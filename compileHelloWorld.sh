mkdir -p helloworld

haxe -main haxe.HelloWorld -cpp helloworld/helloworld
haxe -main haxe.HelloWorld -lua helloworld/helloworld.lua
haxe -main haxe.HelloWorld -neko helloworld/helloworld.n
haxe -main haxe.HelloWorld -python helloworld/helloworld.py
haxe -main haxe.HelloWorld -lib hxnodejs -js helloworld/helloworld.js
haxe -main haxe.HelloWorld -java helloworld/helloworld.jar
