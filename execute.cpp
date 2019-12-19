#include <iostream>
#include <windows.h>
int main() {
    ShellExecute(NULL, "open", "JWL.exe", NULL, NULL, SW_SHOWDEFAULT);
}
