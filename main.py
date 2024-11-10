from bitcode_expression.relationships import (
    expr1, expr2, expr3, expr4, expr5, expr6, expr7, expr8, expr9, expr10,
    expr11, expr12, expr13, expr14, expr15, expr16, expr17, expr18, expr19,
    supplement1, supplement2, supplement3, supplement4, supplement5,
    supplement6, supplement7, supplement8, final_expr
)

if __name__ == "__main__":
    print("Universal Expressions:")
    expressions = [
        expr1, expr2, expr3, expr4, expr5, expr6, expr7, expr8, expr9,
        expr10, expr11, expr12, expr13, expr14, expr15, expr16, expr17,
        expr18, expr19
    ]
    for i, expr in enumerate(expressions, start=1):
        print(f"Expression {i}: {expr}")
        
    print("\nSupplemental Expressions:")
    supplements = [
        supplement1, supplement2, supplement3, supplement4, supplement5,
        supplement6, supplement7, supplement8
    ]
    for i, expr in enumerate(supplements, start=1):
        print(f"Supplement {i}: {expr}")
        
    print("\nFinal Summary in Symbols:")
    print(f"{final_expr}")

    # Keep the console open
    input("\nPress Enter to close the program...")
