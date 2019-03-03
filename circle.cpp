#include <math.h>
#include <iostream>
#include <fstream>
#define PI  3.141592653589793238f
#define DEG2RAD PI/180

using namespace std;
void print_default();

ofstream outputFile;
int main()
{
  // CHANGE HERE!
  int numPoints = 15;
  float radius = 8.5;
  
  outputFile.open("output.txt");
  outputFile.precision(3);
  float x;
  float y;
  float new_x;
  float new_y;
  float delta_x;
  float delta_y;
  cout << "Begin" << endl;
  for(int angle = 0; angle < 360; angle=angle+360/numPoints)
  {
    if(angle == 0)
    {
      outputFile << "G01 Y-" << int(radius) << " F400\r\n";
      x = cos(angle*DEG2RAD) * radius;
      y = sin(angle*DEG2RAD) * radius;
      print_default();
    }
    else
    {
      new_x = cos(angle*DEG2RAD) * radius;
      new_y = sin(angle*DEG2RAD) * radius;
      // Calculate how much to move
      delta_x = (new_y - y) * -1;
      delta_y = (new_x - x) * -1;
      if(delta_x < 0.01 && delta_x > -0.01)
        delta_x = 0;
      if(delta_y < 0.01 && delta_y > -0.01)
        delta_y = 0;
      //outputFile << "G01 X" << delta_x << " F400\r\n";
      //outputFile << "G01 Y" << delta_y << " F400\r\n";
      outputFile << "G01 X" << delta_x << " Y" << delta_y << " F400\r\n";
      print_default();
      // Update x, y values
      x = new_x;
      y = new_y;
    }
  }
  //outputFile << "G01 X" << y << " F400\r\n";
  //outputFile << "G01 Y" << x << " F400\r\n";
  outputFile << "G01 X" << y << " Y" << x << " F400\r\n";
   

  outputFile.close();
  cout << "Done" << endl;
  return 0;
}

void print_default()
{
  outputFile << "M10\r\n";
  outputFile << "M11\r\n";
  outputFile << "G01 Z-5.0 F1000\r\n";
  outputFile << "G01 Z-1.0 F100\r\n";
  outputFile << "G01 Z1.0 F100\r\n";
  outputFile << "G01 Z5.0 F1000\r\n";
}
