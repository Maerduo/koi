
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xbf\xab\xf7f\xbdY\xcf\xe7tl\xd6\xf7Y\xc8\x86\xeb'
    
_lr_action_items = {'OR':([1,3,4,6,9,10,12,13,18,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,51,54,],[-23,-1,-22,-16,21,-17,-18,-10,21,-19,-20,-14,-21,-4,-28,-30,-27,-29,-3,-2,-8,-6,-12,-13,-9,-5,-7,-25,-15,-11,]),'LT':([1,4,11,13,],[-23,-22,23,-10,]),'EXPECTED_DELIVERY_DATE':([0,5,21,22,23,24,26,27,],[1,1,1,1,1,1,1,1,]),'RIGHT_PAREN':([1,3,4,6,10,12,13,18,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,51,53,54,],[-23,-1,-22,-16,-17,-18,-10,33,-19,-20,-14,-21,-4,-28,-30,-27,-29,-3,-2,-8,-6,-12,-13,-9,-5,-7,-25,-15,54,-11,]),'CREATION_DATE':([0,5,21,22,23,24,26,27,],[4,4,4,4,4,4,4,4,]),'EQUALS':([2,7,8,14,],[15,-24,19,28,]),'MONTH_BEFORE':([25,],[42,]),'IS':([8,],[20,]),'TRUE':([19,20,],[34,36,]),'LEFT_PAREN':([0,5,21,22,25,],[5,5,5,5,45,]),'TILDE':([2,7,14,],[16,-24,-26,]),'FALSE':([19,20,],[35,37,]),'PART_DESCRIPTION':([0,5,21,22,],[7,7,7,7,]),'ORDER_ACTIVE':([0,5,21,22,],[8,8,8,8,]),'$end':([1,3,4,6,9,10,12,13,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,51,54,],[-23,-1,-22,-16,0,-17,-18,-10,-19,-20,-14,-21,-4,-28,-30,-27,-29,-3,-2,-8,-6,-12,-13,-9,-5,-7,-25,-15,-11,]),'IN':([1,2,4,7,11,13,14,],[-23,17,-22,-24,25,-10,-26,]),'AFTER':([1,4,11,13,],[-23,-22,26,-10,]),'BEFORE':([1,4,11,13,],[-23,-22,27,-10,]),'GT':([1,4,11,13,],[-23,-22,24,-10,]),'COMMA':([31,32,50,51,],[-14,49,52,-15,]),'STRING':([15,16,17,28,49,],[29,30,31,48,51,]),'DATE':([0,5,21,22,23,24,26,27,45,52,],[13,13,13,13,13,13,13,13,50,53,]),'CURRENT_MONTH':([25,],[43,]),'SUPPLIER_NAME':([0,5,21,22,],[14,14,14,14,]),'AND':([1,3,4,6,9,10,12,13,18,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,51,54,],[-23,-1,-22,-16,22,-17,-18,-10,22,-19,-20,-14,-21,-4,-28,-30,-27,-29,-3,-2,-8,-6,-12,-13,-9,-5,-7,-25,-15,-11,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'date_term':([0,5,21,22,23,24,26,27,],[11,11,11,11,40,41,46,47,]),'list':([17,],[32,]),'date_after_expression':([0,5,21,22,],[6,6,6,6,]),'bool_expression':([0,5,],[9,18,]),'date_in_period_expression':([0,5,21,22,],[12,12,12,12,]),'date_before_expression':([0,5,21,22,],[10,10,10,10,]),'term':([0,5,21,22,],[3,3,38,39,]),'period_term':([25,],[44,]),'text_term':([0,5,21,22,],[2,2,2,2,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> bool_expression","S'",1,None,None,None),
  ('bool_expression -> term','bool_expression',1,'p_expression_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',237),
  ('bool_expression -> bool_expression AND term','bool_expression',3,'p_and_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',243),
  ('bool_expression -> bool_expression OR term','bool_expression',3,'p_or_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',248),
  ('term -> LEFT_PAREN bool_expression RIGHT_PAREN','term',3,'p_term_parenthesis','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',254),
  ('date_after_expression -> date_term AFTER date_term','date_after_expression',3,'p_date_after_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',260),
  ('date_after_expression -> date_term GT date_term','date_after_expression',3,'p_date_after_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',261),
  ('date_before_expression -> date_term BEFORE date_term','date_before_expression',3,'p_date_before_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',266),
  ('date_before_expression -> date_term LT date_term','date_before_expression',3,'p_date_before_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',267),
  ('date_in_period_expression -> date_term IN period_term','date_in_period_expression',3,'p_date_in_period_expression','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',272),
  ('date_term -> DATE','date_term',1,'p_date_term_encoded','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',279),
  ('period_term -> LEFT_PAREN DATE COMMA DATE RIGHT_PAREN','period_term',5,'p_period_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',285),
  ('period_term -> MONTH_BEFORE','period_term',1,'p_period_function_month_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',290),
  ('period_term -> CURRENT_MONTH','period_term',1,'p_period_function_current_month_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',297),
  ('list -> STRING','list',1,'p_string_list','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',305),
  ('list -> list COMMA STRING','list',3,'p_string_list_l','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',311),
  ('term -> date_after_expression','term',1,'p_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',317),
  ('term -> date_before_expression','term',1,'p_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',318),
  ('term -> date_in_period_expression','term',1,'p_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',319),
  ('term -> text_term EQUALS STRING','term',3,'p_string_eql_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',323),
  ('term -> text_term TILDE STRING','term',3,'p_string_tilde_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',327),
  ('term -> text_term IN list','term',3,'p_in_list_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',331),
  ('date_term -> CREATION_DATE','date_term',1,'p_creation_date_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',351),
  ('date_term -> EXPECTED_DELIVERY_DATE','date_term',1,'p_expected_delivery_date_term','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',355),
  ('text_term -> PART_DESCRIPTION','text_term',1,'p_part_description','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',359),
  ('term -> SUPPLIER_NAME EQUALS STRING','term',3,'p_supplier_name_equals','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',363),
  ('text_term -> SUPPLIER_NAME','text_term',1,'p_supplier_name','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',370),
  ('term -> ORDER_ACTIVE IS TRUE','term',3,'p_order_is_active','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',375),
  ('term -> ORDER_ACTIVE EQUALS TRUE','term',3,'p_order_is_active','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',376),
  ('term -> ORDER_ACTIVE IS FALSE','term',3,'p_order_is_not_active','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',380),
  ('term -> ORDER_ACTIVE EQUALS FALSE','term',3,'p_order_is_not_active','C:\\PORT-STC\\PRIVATE\\PL\\horse\\koi\\datalayer\\supply_order_query_parser.py',381),
]