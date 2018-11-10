/**
 * Main - creates two GUIs and one Controller
 * 1 Create GUI object for each GUI
 * 2 IF want to make use of non static logic methods - and create a Logic object
 * 3 Create Controller object and pass in GUI variables so Controller can listen and refer to them (and perhaps Logic variable)
 */
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

import java.awt.geom.*;


public class Main
{
    

    
    
    public static void main(String[] args)
    {
        /** 
         * The following variables, space, width and height are arbitrary dimensions, which
         * make the structure of GUIs and changing them will affect
         * all of the GUIs. This feature can be used later on to 
         * zoom in and out as an extension.
         */
        int space = 20, width = 200, height =30;
        //Colours are passed from here to all of the GUIs and JPanels.
        Color LabelColor= Color.decode("#000d2d")
        , BackColor = Color.WHITE; 
        
        GUIStarter win1 = new GUIStarter(space,width,height,LabelColor,BackColor);
        
        Controller con = new Controller(win1);
        
        win1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        win1.setVisible(true);
        
    }//end main    
    
}//end class Main