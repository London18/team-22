import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import javax.swing.*;
import javax.swing.event.*;
import javax.imageio.ImageIO;
import java.io.*;

public class StarterPane extends JPanel
{
    JLabel jlIntro = new JLabel("Brain Tumour");
    JTextField jtfa = new JTextField(10);
    JLabel jlIntro2 = new JLabel("Manoeuvres AI Simulator");
    JLabel jlChoose = new JLabel("Please Choose one of");
    JLabel jlChoose2 = new JLabel("the following Options");
    JButton jbUpdate = new JButton("Update the Offline Database");
    JButton jbShowVelPos = new JButton ("Register New Candidate");
    JButton jbAbout = new JButton("Contact Us");
    JButton jbExit = new JButton("Exit");



    public StarterPane(int space,int width,int height,Color LabelColor,Color BackColor)
    {
        
        jlIntro.setBounds((int)(1.25*space),space,3*width,height);
        jlIntro2.setBounds((int)(2*space),2*space,3*width,height);
        jlChoose.setBounds((int)(2.5*space),2*space+2*height,width,height);
        jlChoose2.setBounds((int)(2.5*space),3*space+2*height,width,height);
        jbShowVelPos.setBounds((int)5*space,5*space+3*height,width,height);
        jbUpdate.setBounds((int)5*space,6*space+4*height,width,height);
        jbAbout.setBounds((int)5*space,8*space+6*height,width,height);
       
        // Exit Button should be half as wide as the other buttons
        int ExitWidth = width/2;
        jbExit.setBounds((int)(5*space+0.25*width),9*space+7*height,ExitWidth,height);
        
        this.setBackground(BackColor);
        jlIntro.setForeground(Color.white);
        jlIntro2.setForeground(Color.white);
        jlChoose.setForeground(LabelColor);
        jlChoose2.setForeground(LabelColor);
        try{
            BufferedImage Logo = ImageIO.read(new File("./logo.jpg"));
            JLabel label = new JLabel(new ImageIcon(Logo));
            label.setBounds(0,space,2*width,4*height);
            super.add(label);
        } catch(IOException ex){System.out.println("Ex");}
        jbShowVelPos.setBackground(LabelColor);
        jbAbout.setBackground(LabelColor);
        jbUpdate.setBackground(LabelColor);
        jbExit.setBackground(LabelColor);
        
        jbShowVelPos.setForeground(BackColor);
        jbAbout.setForeground(BackColor);
        jbUpdate.setForeground(BackColor);
        jbExit.setForeground(BackColor);
        
        add(jlIntro);
        add(jlIntro2);
        //add(jlChoose);
        //add(jlChoose2);
        add(jbShowVelPos);
        add(jbUpdate);
        add(jbAbout);
        add(jbExit);

    }// end of constructor of the class StarterPane
}//end of the class StarterPane
