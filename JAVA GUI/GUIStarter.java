import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;


public class GUIStarter extends JFrame
{
    StarterPane sp;
    int spheight,spwidth;
    int space,width,height;
    Color LabelColor,BackColor;
    
    //Constructor
    public GUIStarter(int space,int width,int height,Color LabelColor,Color BackColor)
    {
        super("Taylor Jones Partnership");
        this.space = space;
        this.height = height;
        this.width = width;
        this.LabelColor = LabelColor;
        this.BackColor = BackColor;
        
        spheight = 11*space+11*height;
        spwidth = space + 2*width;
        sp = new StarterPane(space,width,height,LabelColor,BackColor);
        sp.setLayout(null);
        sp.setLocation(0,0);
        
        this.setSize(spwidth,spheight);
        this.setLayout(null);
        this.setLocation(0,0);
        this.setContentPane(sp);
    }// end of constructor

}//end of GUIStarter class
