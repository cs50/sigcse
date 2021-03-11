import check50

@check50.check()
def responds_to_Brian():
    """responds to Brian"""
    check50.run("clang hello.c -o hello -lcs50").exit(0)
    check50.run("./hello").stdin("Brian", prompt=False).stdout("hello, Brian\n", regex=False).exit(0)

@check50.check()
def responds_to_Veronica():
    """responds to Veronica"""
    check50.run("clang hello.c -o hello -lcs50").exit(0)
    check50.run("./hello").stdin("Veronica", prompt=False).stdout("hello, Veronica\n", regex=False).exit(0)