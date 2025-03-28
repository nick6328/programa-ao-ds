       IDENTIFICATION DIVISION.
       PROGRAM-ID. SomaSimples.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 NUMERO-1        PIC 9(4).
       01 NUMERO-2        PIC 9(4).
       01 SOMA            PIC 9(5).

       PROCEDURE DIVISION.
           DISPLAY "Digite o primeiro número: " WITH NO ADVANCING.
           ACCEPT NUMERO-1.
           DISPLAY "Digite o segundo número: " WITH NO ADVANCING.
           ACCEPT NUMERO-2.
           
           COMPUTE SOMA = NUMERO-1 + NUMERO-2.
           
           DISPLAY "A soma de " NUMERO-1 " e " NUMERO-2 " é " SOMA.
           STOP RUN.
