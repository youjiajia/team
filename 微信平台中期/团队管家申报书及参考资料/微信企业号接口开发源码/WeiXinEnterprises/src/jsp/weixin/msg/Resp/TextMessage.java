package jsp.weixin.msg.Resp;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * �ı���Ϣ
 * Autohr Engineer.Jsp
 * Date 2014.10.08*/
public class TextMessage extends BaseMessage{
	// �ظ�����Ϣ����  
    private String Content;  
  
    public String getContent() {  
        return Content;  
    }  
  
    public void setContent(String content) {  
        Content = content;  
    }  
    /** 
     * ��ע���Ͳ���
     *  
     * @return 
     */  
    public static String getMainMenu() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue409������ѧ�Բ��Ի����ˣ���ظ�����ѡ�����").append("\n\n");  
        buffer.append("\ue21c  �ұ��˼Ҳ���").append("\n");  
        buffer.append("\ue21d  ��С���ӵ���").append("\n");  
        buffer.append("\ue21e  ������������").append("\n");  
        buffer.append("\ue21f  �������ɵ��").append("\n\n");  
        buffer.append("�ظ���?�����ز˵�");  
        return buffer.toString();  
    } 
    public static String getMenu1() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue402���˼Ҳ�����Ҳ�ң�").append("\n");  
        buffer.append("��ʲô����").append("\n");  
        buffer.append("������").append("\n");  
        buffer.append("���Ѿ��ٱ����ˣ�\ue152").append("\n");  
        buffer.append("��׼������ƨƨ�ɣ�").append("\n\n");  
        buffer.append("�ظ���?�����ز˵�");  
        return buffer.toString();  
    }
    public static String getMenu2() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue108С���ӵĶ�����Ҳ����").append("\n");  
        buffer.append("��ʲô���ʣ�").append("\n");  
        buffer.append("ʲô��Ϊ��").append("\n");  
        buffer.append("�´�Ҫ�ǻ�������").append("\n");  
        buffer.append("�����˽����ң�\ue404").append("\n\n");  
        buffer.append("�ظ���?�����ز˵�");  
        return buffer.toString();  
    }
    public static String getMenu3() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue40e����������ʲô˼�룿").append("\n");  
        buffer.append("��ô�ظ�����˵���").append("\n");  
        buffer.append("��˿���ʱ�¶���ɣ�").append("\n");  
        buffer.append("��Ȼ������Ϊ�ܿɳܣ�").append("\n");  
        buffer.append("����������ԡ�������Ҳ�룡\ue056").append("\n\n");  
        buffer.append("�ظ���?�����ز˵�");  
        return buffer.toString();  
    }
    public static String getMenu4() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue413������û���㣡").append("\n");  
        buffer.append("����ôϲ�����ˣ�").append("\n");  
        buffer.append("������ܶ�����").append("\n");  
        buffer.append("�走���Ҿ����������").append("\n");  
        buffer.append("����o(����)o ��\ue406").append("\n\n");  
        buffer.append("�ظ���?�����ز˵�");  
        return buffer.toString();  
    }
    /** 
     * �����㲥ʹ��ָ�� 
     *  
     * @return 
     */ 
    public static String getMusic() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue03eѧ�Ը����㲥����ָ��").append("\n\n");  
        buffer.append("�ظ�������+����").append("\n");  
        buffer.append("���磺�������").append("\n");  
        buffer.append("���ߣ��������@������").append("\n\n");  
        buffer.append("�ظ���?����ʾ���˵�");  
        return buffer.toString();  
    }
    /** 
     * Q��ͨʹ��ָ�� 
     *  
     * @return 
     */  
    public static String getTranslateUsage() {  
        StringBuffer buffer = new StringBuffer();  
//      buffer.append(XiaoqUtil.emoji(0xe148)).append("Q��ͨʹ��ָ��").append("\n\n"); 
        buffer.append("\ue00cѧ�Է���ʹ��ָ��").append("\n\n");
        buffer.append("��ͨΪ�û��ṩרҵ�Ķ����Է������Ŀǰ֧�����·��뷽��").append("\n");  
        buffer.append("\ue513   �� -> Ӣ\ue510").append("\n");  
        buffer.append("\ue510   Ӣ -> ��\ue513").append("\n");  
        buffer.append("\ue50b   �� -> ��\ue513").append("\n\n");  
        buffer.append("\ue231ʹ��ʾ����").append("\n");  
        buffer.append("    �������ǹ���ʦ").append("\n");  
        buffer.append("    ����engineer").append("\n");  
        buffer.append("    ���뤵�褦�ʤ�").append("\n\n");  
        buffer.append("�ظ���?����ʾ���˵�");  
        return buffer.toString();  
    }
    /** 
     * �����������˵� 
     */  
    public static String getPersonFace() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue001ѧ���������ʹ��ָ��").append("\n\n");  
        buffer.append("\ue008����һ����������Ƭ�����ܰ�����������塢���䡢�Ա����Ϣ").append("\n");  
        buffer.append("�����������ǲ��ǳ���̫�ż�\ue004").append("\n");
        buffer.append("�ظ���?�����ز˵�");
        return buffer.toString();  
    }
//    respContent = "<a href=\"http://www.baidu.com/\">Э�ɹ���</a>";
    public static String getGamesMenu() {  
        StringBuffer buffer = new StringBuffer();  
        buffer.append("\ue00a����ѧ�Բ��Ի����ˣ���ѡ����Ҫ�����Ϸ").append("\n");  
        buffer.append("<a href=\"http://www.yi588.com/h5Game/plappybird/index.html\">������</a>").append("\n");  
        buffer.append("<a href=\"http://www.yi588.com/h5Game/2048/index.html\">2048</a>").append("\n");  
        buffer.append("<a href=\"http://www.yi588.com/h5Game/memory-play/index.html\">��������</a>").append("\n");  
        buffer.append("<a href=\"http://www.yi588.com/h5Game/doudizhu/index.html\">������</a>").append("\n\n");  
        buffer.append("�ظ���?�����ز˵�");  
        return buffer.toString();  
    }
    /** 
     * �ж��Ƿ���QQ���� 
     *  
     * @param content 
     * @return 
     */  
    public static boolean getQQFace(String content) {  
        boolean result = false;  
      
        // �ж�QQ�����������ʽ  
        String qqfaceRegex = "/::\\)|/::~|/::B|/::\\||/:8-\\)|/::<|/::\\$|/::X|/::Z|/::'\\(|/::-\\||/::@|/::P|/::D|/::O|/::\\(|/::\\+|/:--b|/::Q|/::T|/:,@P|/:,@-D|/::d|/:,@o|/::g|/:\\|-\\)|/::!|/::L|/::>|/::,@|/:,@f|/::-S|/:\\?|/:,@x|/:,@@|/::8|/:,@!|/:!!!|/:xx|/:bye|/:wipe|/:dig|/:handclap|/:&-\\(|/:B-\\)|/:<@|/:@>|/::-O|/:>-\\||/:P-\\(|/::'\\||/:X-\\)|/::\\*|/:@x|/:8\\*|/:pd|/:<W>|/:beer|/:basketb|/:oo|/:coffee|/:eat|/:pig|/:rose|/:fade|/:showlove|/:heart|/:break|/:cake|/:li|/:bome|/:kn|/:footb|/:ladybug|/:shit|/:moon|/:sun|/:gift|/:hug|/:strong|/:weak|/:share|/:v|/:@\\)|/:jj|/:@@|/:bad|/:lvu|/:no|/:ok|/:love|/:<L>|/:jump|/:shake|/:<O>|/:circle|/:kotow|/:turn|/:skip|/:oY|/:#-0|/:hiphot|/:kiss|/:<&|/:&>";  
        Pattern p = Pattern.compile(qqfaceRegex);  
        Matcher m = p.matcher(content);  
        if (m.matches()) {  
            result = true;  
        }  
        return result;  
    }
    /** 
     * emoji����ת��(hex -> utf-16) 
     *  
     * @param hexEmoji 
     * @return
     * U+�滻Ϊ0x����X�� 
     */  
    public static String emoji(int hexEmoji) {  
        return String.valueOf(Character.toChars(hexEmoji));  
    }
    /**
     * ���Ц������*/
	public static String weixinJoke(){
		String result = "\ue40dû�м��ص�Ц������Ү";
		Random ran = new Random();
		String content = null;
		String[] _result;
		File file = new File("/mnt/win_d/WebRoot/app/upload/userimages/Joke.txt");
//		File file = new File("http://112.124.111.3/weixinClient/Joke.txt");
		try {
			//
			if(file.isFile()&&file.exists()){
				InputStreamReader input = new InputStreamReader(new FileInputStream(file),"utf-8");
				BufferedReader reader = new BufferedReader(input);
				String line;
				while((line=reader.readLine())!=null ){
				     content +=line;
				}
				_result = content.split("@");
				int count = ran.nextInt(10);
				result = _result[count];
				if(result.startsWith("null")){
					result = result.replace("null", "").trim();
				}
				reader.close();
			}
			//
		} catch (Exception e) {
		}
		return result;
	}
	public static String getLocation() {
		StringBuffer buffer = new StringBuffer();
		buffer.append("\ue036  ѧ���ܱ�ʹ��˵��").append("\n\n");
		buffer.append("1�����͵���λ��").append("\n");
		buffer.append("������ڵײ��ġ�+����ť��ѡ��λ�á����㡰���͡�").append("\n\n");
		buffer.append("2��ָ���ؼ�������").append("\n");
		buffer.append("��ʽ���ܱ�+�ؼ��ʣ�����:\n�ܱ�ATM\ue154\n�ܱ�KTV\ue03c\n�ܱ߲���\ue309\n");
		return buffer.toString();
	}
	public static String RobotService() {
		StringBuffer buffer = new StringBuffer();
		buffer.append("\ue052  ѧ�԰����ܻ�����Ϊ���������ǿ�ʼ�����").append("\n\n");
		buffer.append("\ue231  ����Ц��").append("\n");
		buffer.append("\ue231  ��ʷ����").append("\n");
		buffer.append("\ue231  �ܱ�").append("\n");
		buffer.append("�ظ���?����ʾ���˵�");
		return buffer.toString();
	}
	public static String GetBusService() {
		StringBuffer buffer = new StringBuffer();
		buffer.append("\ue159  ѧ�Թ�����ѯΪ�����񣬰�������ʾ�ظ���ѯ").append("\n\n");
		buffer.append("\ue234  ѧ�Թ�����·��ѯ:").append("\n");
		buffer.append("  ����:����-��·��").append("\n");
		buffer.append("  ��ʾ:��ɳ-159").append("\n\n");
		buffer.append("\ue234  ѧ�Թ������˲�ѯ:").append("\n");
		buffer.append("  ����:���У����-�յ�").append("\n");
		buffer.append("  ��ʾ:��ɳ��������-����֮��").append("\n");
		buffer.append("�ظ���?����ʾ���˵�");
		return buffer.toString();
	}
	public static String GetWeatherService() {
		StringBuffer buffer = new StringBuffer();
		buffer.append("\ue049  ѧ��������ѯΪ�����񣬰�������ʾ�ظ���ѯ").append("\n\n");
		buffer.append("  ����:��������").append("\n");
		buffer.append("  ��ʾ:��ɳ����").append("\n\n");
		buffer.append("�ظ���?����ʾ���˵�");
		return buffer.toString();
	}
	public static String GetTrainService() {
		StringBuffer buffer = new StringBuffer();
		buffer.append("\ue039  ѧ�Ի𳵲�ѯΪ�����񣬰�������ʾ�ظ���ѯ").append("\n\n");
		buffer.append("\ue231�𳵳��β�ѯ:").append("\n");
		buffer.append("  ����:�𳵳���").append("\n");
		buffer.append("  ��ʾ:��T289").append("\n\n");
		buffer.append("\ue231�𳵳�Ʊ��ѯ:").append("\n");
		buffer.append("  ����:��վ����վ,��ѯ�����Ʊ").append("\n");
		buffer.append("  ��ʾ:��ɳ������,2014-07-30").append("\n\n");
		buffer.append("�ظ���?����ʾ���˵�");
		return buffer.toString();
	}
	public static String GetExpressService() {
		StringBuffer buffer = new StringBuffer();
		buffer.append("\ue42f  ѧ�Կ�ݲ�ѯΪ�����񣬰�������ʾ�ظ���ѯ").append("\n\n");
		buffer.append("  ����:�������-����").append("\n");
		buffer.append("  ��ʾ:˳��-575677355677").append("\n\n");
		buffer.append("�ظ���?����ʾ���˵�");
		return buffer.toString();
	}
	public static void main(String[] args) {
		System.out.println(weixinJoke());
	}
}
