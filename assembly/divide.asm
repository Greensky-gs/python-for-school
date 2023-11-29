      // Numerator
      MOV R0, #10
      // Denominator
      MOV R1, #5
      // Temp numerator
      MOV R3, R0
      // Quotient
      MOV R4, #0
      // Rest
      MOV R5, #0
      B division
division:
      ADD R2, R3, #1
      CMP R2, R1
      BGT divide
      MOV R5, R3
      B fin
divide:
      ADD R4, R4, #1
      SUB R3, R3, R1
      B division
fin:
      STR R4, 100
      STR R5, 101
      HALT
