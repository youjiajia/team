package jsp.weixin.menu.util;

/** 
 * �˵��������� 
 *  
 *@author Engineer-Jsp 
 *@date 2014.10.09 
 */  
import jsp.weixin.ParamesAPI.util.AccessToken;
import jsp.weixin.ParamesAPI.util.WeixinUtil;
public class MenuManager {  
  
    public static void main(String[] args) { 
        // ��ҵId  
        String CorpID = "wx52d22b7993b73a6a";  
        // �������ƾ֤��Կ��ÿ��secret�����˶�Ӧ�á�ͨѶ¼���ӿڵĲ�ͬȨ�ޣ���ͬ�Ĺ�����ӵ�в�ͬ��secret 
        String Secret = "63315b00c9b3bc0f67951ddcc372ea11";  
  
        // ���ýӿڻ�ȡaccess_token  
        AccessToken at = WeixinUtil.getAccessToken(CorpID, Secret);  
  
        if (null != at) {  
            // ���ýӿڴ����˵�  
            int result = WeixinUtil.createMenu(getMenu(), at.getToken());  
  
            // �жϲ˵��������  
            if (0 == result){  
            	System.out.println("�˵������ɹ���");
            }else  
            	System.out.println("�˵�����ʧ�ܣ�");
        }  
    }  
  
    /** 
     * ��װ�˵����� 
     *  
     * @return 
     */  
    private static Menu getMenu() {  
        CommonButton btn11 = new CommonButton();  
        btn11.setName("ѧ������");  
        btn11.setType("click");  
        btn11.setKey("11");  
  
        CommonButton btn12 = new CommonButton();  
        btn12.setName("ѧ�Թ���");  
        btn12.setType("click");  
        btn12.setKey("12");  
  
        CommonButton btn13 = new CommonButton();  
        btn13.setName("ѧ���ܱ�");  
        btn13.setType("click");  
        btn13.setKey("13");  
        
        CommonButton btn14 = new CommonButton();  
        btn14.setName("ѧ�Ի�");  
        btn14.setType("click");  
        btn14.setKey("14");
  
        CommonButton btn15 = new CommonButton();  
        btn15.setName("��ʷ����");  
        btn15.setType("click");  
        btn15.setKey("15"); 
        
      
  
        CommonButton btn21 = new CommonButton();  
        btn21.setName("ѧ�Ե㲥");  
        btn21.setType("click");  
        btn21.setKey("21");  
  
        CommonButton btn22 = new CommonButton();  
        btn22.setName("ѧ����Ϸ");  
        btn22.setType("click");  
        btn22.setKey("22");  
  
        CommonButton btn23 = new CommonButton();  
        btn23.setName("ѧ�Է���");  
        btn23.setType("click");  
        btn23.setKey("23");  
  
        CommonButton btn24 = new CommonButton();  
        btn24.setName("�������");  
        btn24.setType("click");  
        btn24.setKey("24");  
  
        CommonButton btn25 = new CommonButton();  
        btn25.setName("ѧ�����");  
        btn25.setType("click");  
        btn25.setKey("25");  
  
//        CommonButton btn31 = new CommonButton();  
//        btn31.setName("��Ȩ����");  
//        btn31.setType("click");  
//        btn31.setKey("31");  
        
      ViewButton btn31 = new ViewButton();  
      btn31.setName("ѧ����Ȩ");  
      btn31.setType("view");  
      btn31.setUrl("http://112.124.111.3/jialian/");
  
  
        CommonButton btn32 = new CommonButton();  
        btn32.setName("ѧ�Կ��");  
        btn32.setType("click");  
        btn32.setKey("32");  
  
        CommonButton btn33 = new CommonButton();  
        btn33.setName("ѧ��Ц��");  
        btn33.setType("click");  
        btn33.setKey("33");
        
        ViewButton btn34 = new ViewButton();  
        btn34.setName("ѧ��΢��");  
        btn34.setType("view");  
        btn34.setUrl("http://112.124.111.3/jialian/");
        
        CommonButton btn35 = new CommonButton();  
        btn35.setName("ͼƬ����");  
        btn35.setType("click");  
        btn35.setKey("35");
        
//        ViewButton btn35 = new ViewButton();  
//        btn35.setName("ѧ�Կͷ�");  
//        btn35.setType("view");  
//        btn35.setUrl("http://wpa.qq.com/msgrd?v=3&uin=471644097&site=qq&menu=yes");
  
        ComplexButton mainBtn1 = new ComplexButton();  
        mainBtn1.setName("ѧ������");  
        mainBtn1.setSub_button(new Button[] { btn11, btn12, btn13, btn14 , btn15});  
  
        ComplexButton mainBtn2 = new ComplexButton();  
        mainBtn2.setName("ѧ������");  
        mainBtn2.setSub_button(new Button[] { btn21, btn22, btn23, btn24 , btn25 });  
  
        ComplexButton mainBtn3 = new ComplexButton();  
        mainBtn3.setName("�������");  
        mainBtn3.setSub_button(new Button[] { btn31, btn32, btn33 , btn34 , btn35});  
  
        /** 
         *  
         * ��ĳ��һ���˵���û�ж����˵��������menu����ζ����أ�<br> 
         * ���磬������һ���˵���ǡ��������顱����ֱ���ǡ���ĬЦ��������ômenuӦ���������壺<br> 
         * menu.setButton(new Button[] { mainBtn1, mainBtn2, btn33 }); 
         */  
        Menu menu = new Menu();  
        menu.setButton(new Button[] { mainBtn1, mainBtn2, mainBtn3 });  
  
        return menu;  
    }  
}  
