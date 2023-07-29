import 'dart:math';

String vid(dynamic a, dynamic b, int c){
  if ( (pow(a, 2)+ pow(b, 2) == pow(c, 2)) || (pow(a, 2)+ pow(c, 2) == pow(b, 2)) || (pow(b, 2)+ pow(c, 2) == pow(a, 2))){
    return "Прямоугольный";
  }
  else if ( (pow(a, 2) + pow(b, 2) > pow(c, 2)) || (pow(a, 2)+ pow(c, 2) > pow(b, 2)) || (pow(b, 2)+ pow(c, 2) > pow(a, 2))){
    return "Остроугольный";
  }
  else{
    return "Тупоугольный";
  }
}

void main(){
  int a=8;
  int b=6;
  int c=11;

  if (a+b>c && a+c>b && b+c>a){
    print(true);
    print(vid(a, b, c));
  }
  else{
    print(false);
  }
}