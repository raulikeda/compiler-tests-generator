func test(x bool) int {
  return x;
}
func main() void{
  // Wrong func return type
  printf(test(true));
}