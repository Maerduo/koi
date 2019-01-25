import enum
from datetime import date
from typing import List

from sqlalchemy import Table, Column, Integer, String, Float, MetaData, ForeignKey, Date, DateTime, Sequence, Boolean, LargeBinary, Binary, Index, Numeric, Enum
from sqlalchemy.orm import relationship, backref

from koi.datalayer.sqla_mapping_base import metadata,Base,DATABASE_SCHEMA,MoneyType
from koi.db_mapping import Customer, OrderPart, Employee, id_generator
from koi.doc_manager.documents_mapping import Document



class ImpactApproval(enum.Enum):
    UNDER_CONSTRUCTION = "Under construction"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class TypeConfigDoc(enum.Enum):
    IMPACT = "Impact document"
    PLAN_2D = "Plan 2D"
    PLAN_3D = "Plan 3D"
    PROGRAM = "Programme"

class CRL(enum.Enum):
    C = "À consulter"
    R = "À remplir"
    LC = "À livrer au client"
    RLC = "À remplir et livrer au client"
    LF = "À livrer au fournisseur"
    RLF = "À remplir et livrer au fournisseur"

    def __str__(self):
        return self.value


ImpactApprovalSQLA = Enum(ImpactApproval, schema=DATABASE_SCHEMA, name='impact_approval')
TypeConfigDocSQLA = Enum(TypeConfigDoc, schema=DATABASE_SCHEMA, name='type_config_doc')
CRLSQLA = Enum(CRL, schema=DATABASE_SCHEMA, name='CRL')



class Configuration(Base):
    __tablename__ = 'configurations'
    configuration_id = Column(Integer,id_generator,nullable=False,primary_key=True)

    frozen = Column(Date, default=None)

    # Configuration 0 is the baseline configuration for a given item/item version.
    # As such, it shouldn't require impact documents to be created.
    # Also, it should not be shown as configuration "0" but as "baseline" to the user.

    version = Column(Integer, default=0)

    freezer_id = Column(Integer, ForeignKey(Employee.employee_id))
    article_configuration_id = Column(Integer, ForeignKey("article_configurations.article_configuration_id"))

    freezer = relationship(Employee, uselist=False)

    # A Configuration represents a version of a configuration
    # That version comes to existence because of some impacts
    # which are represented here.
    origins = relationship("ImpactLine", backref=backref("configuration", uselist=False))

    @property
    def is_baseline( self):
        return self.version == 0

    def __init__(self):
        self.version = 0


class EffectiveConfiguration(Base):
    __tablename__ = 'effective_configurations'
    effective_configuration_id = Column(Integer,id_generator,nullable=False,primary_key=True)

    parent_configuration_id = Column(Integer, ForeignKey( Configuration.configuration_id), nullable=False)
    parent_configuration = relationship( Configuration, backref="effective_configurations")

    # WARNING ! There can be several effective configurations tied to the same order part.
    # Why ? Because one can start on a effective configuration EC1 and then realize that
    # it's wrong, moving to another one EC2. But since things may have happened around EC1
    # we have to record it for auditing purpose.
    # SO the rule is : there can be several effective configuration for an order part, but
    # only one of them is active at any time.

    order_part_id = Column(Integer, ForeignKey( OrderPart.order_part_id))
    order_part = relationship(OrderPart)

    # See note about order_part relationship.
    active = Column(Boolean, default=False)

    # We record who created the configuration. The modifications to the confiugration
    # will be represented by configuraion ines which can have many different authors.
    # We go this way because we assume that this entity won't change once created
    # so there's no need to record anyting more than the original author.
    creator_id = Column(Integer, ForeignKey(Employee.employee_id))



class ConfigurationLine(Base):
    __tablename__ = 'configuration_lines'

    configuration_line_id = Column(Integer,id_generator,nullable=False,primary_key=True)

    description = Column(String)

    # Version of the document in this configuration line
    version = Column(Integer, default=0)
    document_id = Column(Integer, ForeignKey(Document.document_id))
    document_type = Column( TypeConfigDocSQLA)
    modify_config = Column(Boolean)
    date_upload = Column(Date)
    crl = Column(CRLSQLA)

    document = relationship(Document, uselist=False) # One-to-one relationship

    configuration_id = Column(Integer, ForeignKey(Configuration.configuration_id), nullable=True)
    configuration = relationship(Configuration, uselist=False, backref="lines" )

    # For the moment I link it this way. It's not clean.
    effective_configuration_id = Column(Integer, ForeignKey(EffectiveConfiguration.effective_configuration_id), nullable=True)
    effective_configuration = relationship(EffectiveConfiguration, uselist=False, backref="lines" )

    # def __init__(self):
    #     self.version = 0


""" solution 1 : muiltiple inheritance
    solution 2 : outside function => won't work with prototype
    solution 3 : add function at code gen time
"""





class ArticleConfiguration(Base):
    """An Article Configuration is mainly made of two things.

    First, a list of impact documents (represented by ImpactLines
    entities).  Each of those describe the context of a confiugration.

    Second, a list of Configuration (represented by Configuration
    entities). Each configuration descibes how to configure the
    factory. This is done with a set of documents (represented by
    ConfigurationLines entities).

    An impact document justifiy the existence of a given configuration.
    Impact documents should normally be created before each configuration
    except for the baseline one (the "revision 0"). But we allow them to
    be created after, for more user firendliness. However, we enforce
    the fact that there must be an impact document (at least one) to
    to freeze a configuration. So when a configuration comes in use
    then we know its documentation is complete as far as the process
    of related to imlpact documents is concerned. An exception is made
    for the baseline configuration. This exists just because of the
    will of the user, and it just requires a plan/part to exist before
    hand. So in that case, we don't request an impact document to
    allow freezing.

    """

    __tablename__ = 'article_configurations'
    article_configuration_id = Column(Integer,id_generator,nullable=False,primary_key=True)

    customer_id = Column(Integer, ForeignKey(Customer.customer_id))
    identification_number = Column(String)
    revision_number = Column(String, default="A")
    date_creation = Column(Date)

    part_plan_id = Column(Integer, ForeignKey(Document.document_id))

    customer = relationship(Customer, uselist=False)
    configurations = relationship( Configuration, order_by=Configuration.version, backref=backref('article_configuration', enable_typechecks=False), enable_typechecks=False)
    part_plan = relationship(Document, uselist=False)


    # Methods defined as static to be reused in DTO objects !
    # and as property to be easily accessible (because static
    # can't be used as properties...)

    # @property
    # def current_configuration(self):
    #     return ArticleConfiguration._current_configuration(self)

    @staticmethod
    def _current_configuration(self):
        i = len(self.configurations) - 1

        if i < 0:
            # 0 element
            return None

        elif i == 0:
            # one element
            self.configurations[0]

        elif i >= 0:
            # At least two elements
            while i >= 0:
                if self.configurations[i].frozen:
                    return self.configurations[i]
                i -= 1

            return self.configurations[-1]


class ImpactLine(Base):
    __tablename__ = 'impact_lines'
    impact_line_id = Column(Integer,id_generator,nullable=False,primary_key=True)

    # Short description of the document.
    # Some unstructured meta information about the document can fit here.
    description = Column(String)

    approval = Column(ImpactApprovalSQLA)
    approval_date = Column(Date)
    active_date = Column(Date)

    # An impact line may not be wired to a configuration.
    # Ultimately, it should end up wired to one, but
    # it may not be the case at time of its creation. That's
    # because one may want to track an impact file before
    # it actually results in a new version of a configuration.
    # Conversely, a configuration may have several impact documents.
    configuration_id = Column(Integer, ForeignKey( Configuration.configuration_id))

    # Even if impact line defines configuration versions, they
    # nonetheless belong to one article configuration.
    article_configuration_id = Column(Integer, ForeignKey(ArticleConfiguration.article_configuration_id),nullable=False)
    article_configuration = relationship(ArticleConfiguration, uselist=False, backref=backref("impacts", enable_typechecks=False), enable_typechecks=False)

    owner_id = Column(Integer, ForeignKey(Employee.employee_id), nullable=False)

    # The approver is set only if the approval state is ImpactApproval.APPROVED.
    approver_id = Column(Integer, ForeignKey(Employee.employee_id))

    document_id = Column(Integer, ForeignKey(Document.document_id), nullable=False)

    document = relationship(Document, uselist=False)



    @staticmethod
    def _version(self):
        """ When an impact file is associated to a configuration,
        it "creates" a version of that configuration. So the
        version of the configuration comes to existence *because*
        of one or more impact lines are wired to the configuration.
        """
        if self.configuration:
            return self.configuration.version
        else:
            return None

    @staticmethod
    def _date_upload(self):
        return self.document.upload_date

# Put here to be able to use foreign_keys parameters
# to desambiguate the two relationships to Employee
ImpactLine.owner = relationship(Employee, uselist=False, foreign_keys=[ImpactLine.owner_id])
ImpactLine.approved_by = relationship(Employee, uselist=False, foreign_keys=[ImpactLine.approver_id])

OrderPart.configuration = relationship(Configuration, backref='parts')
