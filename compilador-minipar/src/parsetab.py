
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN BOOL CHANNEL DIGIT DIVIDE ELSE EQUAL FALSE GE_THAN G_THAN ID IF INPUT INT LBRACE LE_THAN LPAREN L_THAN MINUS NOT_EQUAL OUTPUT PAR_BLOCK PLUS RBRACE RPAREN SEQ_BLOCK STRING STRING_VALUE TIMES TRUE WHILEstmt_block : seq_stmts\n| par_stmts\n| stmt_block seq_stmts\n| stmt_block par_stmtsseq_stmts : SEQ_BLOCK stmtspar_stmts : PAR_BLOCK stmtsstmts : stmt\n| stmts stmtstmt : assignment\n| declaration\n| IF LPAREN condition RPAREN stmt\n| IF LPAREN condition RPAREN stmt ELSE stmt\n| WHILE LPAREN condition RPAREN stmt\n| LBRACE stmts RBRACE\n| funcfunc : INPUT LPAREN RPAREN\n| OUTPUT LPAREN STRING_VALUE RPARENdeclaration  : c_channel\n| b_declaration\n| s_declaration\n| i_declarationcondition  : condition LE_THAN expr\n| condition GE_THAN expr\n| condition L_THAN expr\n| condition G_THAN expr\n| condition EQUAL expr\n| condition NOT_EQUAL expr\n| bool_val\n| exprbool_val : TRUE\n| FALSEassignment : ID ASSIGN expr\n| ID ASSIGN funcexpr : expr PLUS term\n| expr MINUS term\n| termterm : term TIMES factor\n| term DIVIDE factor\n| factorfactor : LPAREN expr RPAREN\n| DIGIT\n| ID\n| STRING_VALUEempty :c_channel : CHANNEL ID ID IDb_declaration : BOOL IDs_declaration : STRING IDi_declaration : INT ID'
    
_lr_action_items = {'SEQ_BLOCK':([0,1,2,3,6,7,8,9,10,11,15,17,18,19,20,27,28,36,37,38,45,46,47,48,49,51,52,53,54,70,71,72,73,80,81,82,83,84,86,],[4,4,-1,-2,-3,-4,-5,-7,-9,-10,-15,-18,-19,-20,-21,-6,-8,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,-17,-45,-40,-11,-34,-35,-37,-38,-13,-12,]),'PAR_BLOCK':([0,1,2,3,6,7,8,9,10,11,15,17,18,19,20,27,28,36,37,38,45,46,47,48,49,51,52,53,54,70,71,72,73,80,81,82,83,84,86,],[5,5,-1,-2,-3,-4,-5,-7,-9,-10,-15,-18,-19,-20,-21,-6,-8,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,-17,-45,-40,-11,-34,-35,-37,-38,-13,-12,]),'$end':([1,2,3,6,7,8,9,10,11,15,17,18,19,20,27,28,36,37,38,45,46,47,48,49,51,52,53,54,70,71,72,73,80,81,82,83,84,86,],[0,-1,-2,-3,-4,-5,-7,-9,-10,-15,-18,-19,-20,-21,-6,-8,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,-17,-45,-40,-11,-34,-35,-37,-38,-13,-12,]),'IF':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[12,12,12,-7,-9,-10,12,-15,-18,-19,-20,-21,12,-8,12,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,12,12,-17,-45,-40,-11,-34,-35,-37,-38,-13,12,-12,]),'WHILE':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[13,13,13,-7,-9,-10,13,-15,-18,-19,-20,-21,13,-8,13,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,13,13,-17,-45,-40,-11,-34,-35,-37,-38,-13,13,-12,]),'LBRACE':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[14,14,14,-7,-9,-10,14,-15,-18,-19,-20,-21,14,-8,14,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,14,14,-17,-45,-40,-11,-34,-35,-37,-38,-13,14,-12,]),'ID':([4,5,8,9,10,11,14,15,17,18,19,20,23,24,25,26,27,28,29,30,31,32,35,36,37,38,39,45,46,47,48,49,51,52,53,54,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,80,81,82,83,84,85,86,],[16,16,16,-7,-9,-10,16,-15,-18,-19,-20,-21,35,36,37,38,16,-8,48,48,16,48,56,-46,-47,-48,48,-36,-39,-41,-42,-43,-14,-32,-33,-16,71,16,48,48,48,48,48,48,48,48,48,48,16,-17,-45,-40,-11,-34,-35,-37,-38,-13,16,-12,]),'INPUT':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,32,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[21,21,21,-7,-9,-10,21,-15,-18,-19,-20,-21,21,-8,21,21,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,21,21,-17,-45,-40,-11,-34,-35,-37,-38,-13,21,-12,]),'OUTPUT':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,32,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[22,22,22,-7,-9,-10,22,-15,-18,-19,-20,-21,22,-8,22,22,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,22,22,-17,-45,-40,-11,-34,-35,-37,-38,-13,22,-12,]),'CHANNEL':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[23,23,23,-7,-9,-10,23,-15,-18,-19,-20,-21,23,-8,23,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,23,23,-17,-45,-40,-11,-34,-35,-37,-38,-13,23,-12,]),'BOOL':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[24,24,24,-7,-9,-10,24,-15,-18,-19,-20,-21,24,-8,24,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,24,24,-17,-45,-40,-11,-34,-35,-37,-38,-13,24,-12,]),'STRING':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[25,25,25,-7,-9,-10,25,-15,-18,-19,-20,-21,25,-8,25,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,25,25,-17,-45,-40,-11,-34,-35,-37,-38,-13,25,-12,]),'INT':([4,5,8,9,10,11,14,15,17,18,19,20,27,28,31,36,37,38,45,46,47,48,49,51,52,53,54,58,69,70,71,72,73,80,81,82,83,84,85,86,],[26,26,26,-7,-9,-10,26,-15,-18,-19,-20,-21,26,-8,26,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,26,26,-17,-45,-40,-11,-34,-35,-37,-38,-13,26,-12,]),'RBRACE':([9,10,11,15,17,18,19,20,28,31,36,37,38,45,46,47,48,49,51,52,53,54,70,71,72,73,80,81,82,83,84,86,],[-7,-9,-10,-15,-18,-19,-20,-21,-8,51,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,-17,-45,-40,-11,-34,-35,-37,-38,-13,-12,]),'ELSE':([10,11,15,17,18,19,20,36,37,38,45,46,47,48,49,51,52,53,54,70,71,72,73,80,81,82,83,84,86,],[-9,-10,-15,-18,-19,-20,-21,-46,-47,-48,-36,-39,-41,-42,-43,-14,-32,-33,-16,-17,-45,-40,85,-34,-35,-37,-38,-13,-12,]),'LPAREN':([12,13,21,22,29,30,32,39,59,60,61,62,63,64,65,66,67,68,],[29,30,33,34,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'ASSIGN':([16,],[32,]),'TRUE':([29,30,],[43,43,]),'FALSE':([29,30,],[44,44,]),'DIGIT':([29,30,32,39,59,60,61,62,63,64,65,66,67,68,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'STRING_VALUE':([29,30,32,34,39,59,60,61,62,63,64,65,66,67,68,],[49,49,49,55,49,49,49,49,49,49,49,49,49,49,49,]),'RPAREN':([33,40,41,42,43,44,45,46,47,48,49,50,55,57,72,74,75,76,77,78,79,80,81,82,83,],[54,58,-29,-28,-30,-31,-36,-39,-41,-42,-43,69,70,72,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'LE_THAN':([40,41,42,43,44,45,46,47,48,49,50,72,74,75,76,77,78,79,80,81,82,83,],[59,-29,-28,-30,-31,-36,-39,-41,-42,-43,59,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'GE_THAN':([40,41,42,43,44,45,46,47,48,49,50,72,74,75,76,77,78,79,80,81,82,83,],[60,-29,-28,-30,-31,-36,-39,-41,-42,-43,60,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'L_THAN':([40,41,42,43,44,45,46,47,48,49,50,72,74,75,76,77,78,79,80,81,82,83,],[61,-29,-28,-30,-31,-36,-39,-41,-42,-43,61,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'G_THAN':([40,41,42,43,44,45,46,47,48,49,50,72,74,75,76,77,78,79,80,81,82,83,],[62,-29,-28,-30,-31,-36,-39,-41,-42,-43,62,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'EQUAL':([40,41,42,43,44,45,46,47,48,49,50,72,74,75,76,77,78,79,80,81,82,83,],[63,-29,-28,-30,-31,-36,-39,-41,-42,-43,63,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'NOT_EQUAL':([40,41,42,43,44,45,46,47,48,49,50,72,74,75,76,77,78,79,80,81,82,83,],[64,-29,-28,-30,-31,-36,-39,-41,-42,-43,64,-40,-22,-23,-24,-25,-26,-27,-34,-35,-37,-38,]),'PLUS':([41,45,46,47,48,49,52,57,72,74,75,76,77,78,79,80,81,82,83,],[65,-36,-39,-41,-42,-43,65,65,-40,65,65,65,65,65,65,-34,-35,-37,-38,]),'MINUS':([41,45,46,47,48,49,52,57,72,74,75,76,77,78,79,80,81,82,83,],[66,-36,-39,-41,-42,-43,66,66,-40,66,66,66,66,66,66,-34,-35,-37,-38,]),'TIMES':([45,46,47,48,49,72,80,81,82,83,],[67,-39,-41,-42,-43,-40,67,67,-37,-38,]),'DIVIDE':([45,46,47,48,49,72,80,81,82,83,],[68,-39,-41,-42,-43,-40,68,68,-37,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt_block':([0,],[1,]),'seq_stmts':([0,1,],[2,6,]),'par_stmts':([0,1,],[3,7,]),'stmts':([4,5,14,],[8,27,31,]),'stmt':([4,5,8,14,27,31,58,69,85,],[9,9,28,9,28,28,73,84,86,]),'assignment':([4,5,8,14,27,31,58,69,85,],[10,10,10,10,10,10,10,10,10,]),'declaration':([4,5,8,14,27,31,58,69,85,],[11,11,11,11,11,11,11,11,11,]),'func':([4,5,8,14,27,31,32,58,69,85,],[15,15,15,15,15,15,53,15,15,15,]),'c_channel':([4,5,8,14,27,31,58,69,85,],[17,17,17,17,17,17,17,17,17,]),'b_declaration':([4,5,8,14,27,31,58,69,85,],[18,18,18,18,18,18,18,18,18,]),'s_declaration':([4,5,8,14,27,31,58,69,85,],[19,19,19,19,19,19,19,19,19,]),'i_declaration':([4,5,8,14,27,31,58,69,85,],[20,20,20,20,20,20,20,20,20,]),'condition':([29,30,],[40,50,]),'expr':([29,30,32,39,59,60,61,62,63,64,],[41,41,52,57,74,75,76,77,78,79,]),'bool_val':([29,30,],[42,42,]),'term':([29,30,32,39,59,60,61,62,63,64,65,66,],[45,45,45,45,45,45,45,45,45,45,80,81,]),'factor':([29,30,32,39,59,60,61,62,63,64,65,66,67,68,],[46,46,46,46,46,46,46,46,46,46,46,46,82,83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> stmt_block","S'",1,None,None,None),
  ('stmt_block -> seq_stmts','stmt_block',1,'p_stmt_block','parser.py',18),
  ('stmt_block -> par_stmts','stmt_block',1,'p_stmt_block','parser.py',19),
  ('stmt_block -> stmt_block seq_stmts','stmt_block',2,'p_stmt_block','parser.py',20),
  ('stmt_block -> stmt_block par_stmts','stmt_block',2,'p_stmt_block','parser.py',21),
  ('seq_stmts -> SEQ_BLOCK stmts','seq_stmts',2,'p_seq_stmts','parser.py',28),
  ('par_stmts -> PAR_BLOCK stmts','par_stmts',2,'p_par_block','parser.py',32),
  ('stmts -> stmt','stmts',1,'p_stmts','parser.py',36),
  ('stmts -> stmts stmt','stmts',2,'p_stmts','parser.py',37),
  ('stmt -> assignment','stmt',1,'p_stmt','parser.py',44),
  ('stmt -> declaration','stmt',1,'p_stmt','parser.py',45),
  ('stmt -> IF LPAREN condition RPAREN stmt','stmt',5,'p_stmt','parser.py',46),
  ('stmt -> IF LPAREN condition RPAREN stmt ELSE stmt','stmt',7,'p_stmt','parser.py',47),
  ('stmt -> WHILE LPAREN condition RPAREN stmt','stmt',5,'p_stmt','parser.py',48),
  ('stmt -> LBRACE stmts RBRACE','stmt',3,'p_stmt','parser.py',49),
  ('stmt -> func','stmt',1,'p_stmt','parser.py',50),
  ('func -> INPUT LPAREN RPAREN','func',3,'p_func','parser.py',64),
  ('func -> OUTPUT LPAREN STRING_VALUE RPAREN','func',4,'p_func','parser.py',65),
  ('declaration -> c_channel','declaration',1,'p_declaration','parser.py',73),
  ('declaration -> b_declaration','declaration',1,'p_declaration','parser.py',74),
  ('declaration -> s_declaration','declaration',1,'p_declaration','parser.py',75),
  ('declaration -> i_declaration','declaration',1,'p_declaration','parser.py',76),
  ('condition -> condition LE_THAN expr','condition',3,'p_condition','parser.py',80),
  ('condition -> condition GE_THAN expr','condition',3,'p_condition','parser.py',81),
  ('condition -> condition L_THAN expr','condition',3,'p_condition','parser.py',82),
  ('condition -> condition G_THAN expr','condition',3,'p_condition','parser.py',83),
  ('condition -> condition EQUAL expr','condition',3,'p_condition','parser.py',84),
  ('condition -> condition NOT_EQUAL expr','condition',3,'p_condition','parser.py',85),
  ('condition -> bool_val','condition',1,'p_condition','parser.py',86),
  ('condition -> expr','condition',1,'p_condition','parser.py',87),
  ('bool_val -> TRUE','bool_val',1,'p_bool_val','parser.py',94),
  ('bool_val -> FALSE','bool_val',1,'p_bool_val','parser.py',95),
  ('assignment -> ID ASSIGN expr','assignment',3,'p_assignment','parser.py',99),
  ('assignment -> ID ASSIGN func','assignment',3,'p_assignment','parser.py',100),
  ('expr -> expr PLUS term','expr',3,'p_expr','parser.py',104),
  ('expr -> expr MINUS term','expr',3,'p_expr','parser.py',105),
  ('expr -> term','expr',1,'p_expr','parser.py',106),
  ('term -> term TIMES factor','term',3,'p_term','parser.py',113),
  ('term -> term DIVIDE factor','term',3,'p_term','parser.py',114),
  ('term -> factor','term',1,'p_term','parser.py',115),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor','parser.py',122),
  ('factor -> DIGIT','factor',1,'p_factor','parser.py',123),
  ('factor -> ID','factor',1,'p_factor','parser.py',124),
  ('factor -> STRING_VALUE','factor',1,'p_factor','parser.py',125),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',132),
  ('c_channel -> CHANNEL ID ID ID','c_channel',4,'p_c_channel','parser.py',136),
  ('b_declaration -> BOOL ID','b_declaration',2,'p_b_declaration','parser.py',140),
  ('s_declaration -> STRING ID','s_declaration',2,'p_s_declaration','parser.py',144),
  ('i_declaration -> INT ID','i_declaration',2,'p_i_declaration','parser.py',148),
]
