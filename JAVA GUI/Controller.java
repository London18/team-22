import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
public class Controller implements ActionListener 
{
    GUIInput input;
    GUIOrbit go;
    GUIStarter gs;
    //constructor
    public Controller(GUIStarter guiStarter)
    {
        // construct the GUI views
        this.gs = guiStarter;
        
        gs.sp.jbSubmit.addActionListener(this);
        
        gs.sp.jbExit.addActionListener(this);

    }//end constructor
    
    public void actionPerformed(ActionEvent ae) 
    {
        if(ae.getSource()==gs.sp.jbExit){
            System.exit(10);
        }
            
            
        if(ae.getSource()==gs.sp.jbAbout){
            
            infoBox(" This program was made by Team 22");
        }
        
        
        // To prevent NullPointerException, I personally prefer this method over try and catch.    
        if(input !=null){
            
            if(ae.getSource()==input.ip.jbClose){
                        System.exit(10);
                }
            try{    
                if (ae.getSource()==input.ip.jbSubmit) 
                   {
                   
                    if(a>=0 || a2>=0){
                        // Eliminating the unshowable, the numbers are correspondent to the information given in the infoBox
                        // but are as well, secure enough to cover any level of precision of radius of earth(down to 2 significant figures).
                        if((a<20000000 || a>192000000) || (a2<20000000 || a2>192000000))
                        {
                            infoBox("The radii of the orbits must be between 4 and 30 radii of earth","Error : Radius Out of Range");
                        }
                        else
                        {
                            pi = new pos(a,0,0,0,0,0);
                            pf = new pos(a2,0,0,0,0,0);
                            
                            hoh = new Hohmann(pi,pf);
                        
                            input.setVisible(false);
                            
                            go = new GUIOrbit(pi,pf,input.space,input.width,input.height,input.LabelColor,input.BackColor);         
                            go.setVisible(true);
                            
                            //Adding ActionListeners to the GUI that has been added here.
                            go.op.jbBack.addActionListener(this);
                            go.op.jbDraw.addActionListener(this);
                            go.op.jbClose.addActionListener(this);
                        }
                        
                    }
                    else{
                        // a little banter, when a negative length is entered.
                        infoBox("Dear time traveller/extraterrestrial being,\nOn earth we still haven't discovered such concept as negative length,\n Accordingly, please enter a positive value.\n\nJoul gyuno gluboraol/ozglugollocglyuur voot,\nEm oulch quo cgyura fubom'g jyucseboloja caseh semsokg uc motugyubo romtch,\n Usseljotri, krouco omgol u kecyugyubo burao.","Error : Negative Length");  
                    }}
                }
            catch(NumberFormatException e){
                // catch any non-number values (including null and letters)
                infoBox("Please input the required data","Error : Wrong Numbers");
            }
            if(ae.getSource()==input.ip.jbBack){
    
                input.setVisible(false);
                gs.setVisible(true);
                }
        }
        

            }
        }
    }             

    //Declaration of a MessageDialog in form of a method to avoid repetition in the above code
    public static void infoBox(String infoMessage, String titleBar)
    {
        JOptionPane.showMessageDialog(null, infoMessage, titleBar, JOptionPane.INFORMATION_MESSAGE);
    }
 
    public static double StringRad(String written){
        
        return Double.parseDouble(written)/180*Math.PI;
        
    }
    
}
