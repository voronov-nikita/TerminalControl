// ignore_for_file: use_key_in_widget_constructors, prefer_const_constructors

import 'package:flutter/material.dart';



class MyAppBar extends StatelessWidget implements PreferredSizeWidget {
  @override
  Size get preferredSize => Size.fromHeight(kToolbarHeight);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      title: Text('My App'),
      centerTitle: true,
      backgroundColor: const Color.fromARGB(255, 152, 34, 25),
      titleTextStyle: TextStyle(
        color: Color.fromARGB(255, 0, 145, 171)
      ),
    );
  }
}


class MyHomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: Text(
          'Welcome to my app!', 
          style: TextStyle(
            color: Colors.white,
            fontSize: 50,
          ),
          ),
      ),
    );
  }
}


class MyCompleteApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "BigMafia",
      home: Scaffold(
        appBar: MyAppBar(),
        body: MyHomePage(),
      ),
    );
  }
}

void main() {
  runApp(MyCompleteApp());
}
