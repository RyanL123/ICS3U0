import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class collage extends PApplet {

ArrayList<PImage> animal_images, landscape_images;
boolean animal = true;
int counter = 0;

public void setup() {
  String [] animals = {"adorable-cat", "bird", "dog", "snake", "turtle", "wasp", "white_bird"};
  String [] landscapes = {"autumn_lake", "canyon", "cliff", "coniferous_forest", "foggy_mountain", "framed_autumn_lake", "mountain", "ocean_side", "river_through_mountains", "water_body_near_trees", "winter_mountain"};
  animal_images = new ArrayList<PImage>();
  landscape_images = new ArrayList<PImage>();
  

  for (int i = 0; i < animals.length; i++) {
    animal_images.add(loadImage(animals[i] + ".jpg"));
  }
  for (int i = 0; i < landscapes.length; i++) {
    landscape_images.add(loadImage(landscapes[i] + ".jpg"));
  }
}

public void draw() {
  background(0);
  // Draw the image to the screen at coordinate (0,0)
  if (animal == true) {
    image(animal_images.get(counter), 0, 0, width, height);
  } else {
    image(landscape_images.get(counter), 0, 0, width, height);
  }
}

public void mouseClicked() {
  if (mouseButton == LEFT) {
    counter++;
  } else if (mouseButton == RIGHT) {
    animal = !animal;
  }
  if (animal == true && counter >= animal_images.size()) {
    counter = 0;
  } else if (animal == false && counter >= landscape_images.size()) {
    counter = 0;
  }
}
  public void settings() {  size(640, 480); }
  public static void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "collage" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
