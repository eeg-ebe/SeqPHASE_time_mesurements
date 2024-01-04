package haxe;

import Sys;

/**
 * Simple Hello World program to check
 * how long different programming languages
 * and operation systems need in order to
 * "boot" a particular program.
 */
class HelloWorld {

    public static function main() {
        Sys.stderr().writeString("Hello World\n");
    }

}
