import sys
def main( ):
  name=input( "what is your name? ")
  if  name.lower()== "brian":
    print("welcome, Brian")
  else:
    print("you aren't brian")
    sys.exit( 1 )
main()

