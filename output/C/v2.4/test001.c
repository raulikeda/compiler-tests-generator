 A int = 2;
func myprint(text str) void{
  printf(text);
}

func fac(x int) int {
  if (x == 1) {
    return 1;
  }
  return x * fac(x-1);
}
func sum(x int, y int) int {
  return x + y;
}

func tautology() bool {
  return true;
}

func main() void{
   x_1 int;
  x_1 = scanf();
   x_2 int = fac(4);
  printf(A); 
  printf(x_2);
  {
     x_2 int = 7;
    x_1 = 9;
    A = 8;
    printf(x_2);
  }
  printf(A);
  printf(x_1);
  
  if ((x_1 > 1 && !!!(x_1 < 1)) || x_1 == 9) {
    x_1 = 2;
  }
  
   x int = 3+6/3   *  2 -+-  +  2*4/2 + 0/1 -((6+ ((4)))/(2)); // Teste // Teste 2
   y_1 int = 3;
  y_1 = sum(y_1, x_1);
   z__ int;
  z__ = x + y_1;
  
  if (x_1 == 2) {
    x_1 = 2;
  }
  
  if (x_1 == 3) {
    x_1 = 2;
  } else {
    x_1 = 3;
  }
  
  x_1 = 0;
  while (x_1 < 1 || x == 2) {
    printf(x_1);
    x_1 = x_1 + 1;
  }
  
  
  ;;;
  // Saida final
  printf(x_1);
  printf(x);
  printf(z__+1);
  
  // All int operations
   y int = 2;
   z int;
  z = (y - 1);
  printf(y+z);
  printf(y-z);
  printf(y*z);
  printf(y/z);
  printf(y == z);
  printf(y < z);
  printf(y > z);
  
  // All str operations 
   a str;
   b str;
  
  x_1 = 1;
  y = 1; 
  z = 2;
  a = "abc";
  b = "def";
  myprint(a.b);
  myprint(a);
  printf(a.x_1);
  printf(x_1.a);
  printf(a.(x_1==1));
  printf(a == a);
  printf(a < b);
  printf(a > b);
}