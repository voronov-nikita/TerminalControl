// ignore_for_file: avoid_print, prefer_const_constructors, unnecessary_string_interpolations, use_key_in_widget_constructors

import 'package:flutter/material.dart';


void main(){
  runApp(MyApp());
}

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){
    String str="o";
    return MaterialApp(
      title: "Hello",
      theme: ThemeData(primaryColor: Colors.amber),
      home: Scaffold(
        backgroundColor: Colors.black,
        appBar: AppBar(
          title: Text("Hello"),
          backgroundColor: Colors.black38,
        ),
        body: Center(
          child: Text('$str', style: TextStyle(
            fontSize: 48,
            fontFamily: 'Times New Roman',
            color: Colors.white,
            )
          ),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () => print("click"),
          backgroundColor: Colors.red,
          child: Text('Ok'),
        ),
      ),
    );
  }
}
