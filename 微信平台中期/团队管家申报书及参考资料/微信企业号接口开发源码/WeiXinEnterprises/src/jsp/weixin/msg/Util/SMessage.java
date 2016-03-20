package jsp.weixin.msg.Util;
/** 
 * ������Ϣ�� 
 * @author Engineer.Jsp
 * @date 2014.10.11 
 */
import java.util.ArrayList;
import java.util.List;
import net.sf.json.JSONArray;
import jsp.weixin.ParamesAPI.util.ParamesAPI;
import jsp.weixin.ParamesAPI.util.WeixinUtil;
import jsp.weixin.msg.Resp.Article;

public class SMessage {
	//���ͽӿ�
	public static String POST_URL = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN";
	/**
	 * text��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��text
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param content ��Ϣ����
	 * @param safe ��ʾ�Ƿ��Ǳ�����Ϣ��0��ʾ��1��ʾ�ǣ�Ĭ��0
	 * */
	public static String STextMsg(String touser,String toparty,String totag,String agentid,String content){
		String PostData = "{\"touser\": %s,\"toparty\": %s,\"totag\": %s,\"msgtype\": \"text\",\"agentid\": %s,\"text\": {\"content\": %s},\"safe\":\"0\"}";
		return String.format(PostData, touser,toparty,totag,agentid,content);
	}
	
	/**
	 * image��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��image
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param media_id ý����Դ�ļ�ID
	 * @param safe ��ʾ�Ƿ��Ǳ�����Ϣ��0��ʾ��1��ʾ�ǣ�Ĭ��0
	 * */
	public static String SImageMsg(String touser,String toparty,String agentid ,String media_id){
		String PostData = "{\"touser\": %s,\"toparty\": %s,\"msgtype\": \"image\",\"agentid\": %s,\"image\": {\"media_id\": %s},\"safe\":\"0\"}";
		return String.format(PostData, touser,toparty,agentid,media_id);
	}
	
	/**
	 * voice��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��voice
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param media_id ý����Դ�ļ�ID
	 * @param safe ��ʾ�Ƿ��Ǳ�����Ϣ��0��ʾ��1��ʾ�ǣ�Ĭ��0
	 * */
	public static String SVoiceMsg(String touser,String toparty,String totag,String agentid ,String media_id){
		String PostData = "{\"touser\": %s,\"toparty\": %s,\"totag\": %s,\"msgtype\": \"voice\",\"agentid\": %s,\"voice\": {\"media_id\": %s},\"safe\":\"0\"}";
		return String.format(PostData, touser,toparty,totag,agentid,media_id);
	}
	
	/**
	 * video��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��video
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param media_id ý����Դ�ļ�ID
	 * @param title ��Ƶ��Ϣ�ı���
	 * @param description ��Ƶ��Ϣ������
	 * @param safe ��ʾ�Ƿ��Ǳ�����Ϣ��0��ʾ��1��ʾ�ǣ�Ĭ��0
	 */
	public static String SVideoMsg(String touser,String toparty,String totag,String agentid,String media_id,String title,String description){
		String PostData = "{\"touser\": %s,\"toparty\": %s,\"totag\": %s,\"msgtype\": \"video\",\"agentid\": %s,\" video\": {\"media_id\": %s,\"title\": %s,\"description\": %s},\"safe\":\"0\"}";
		return String.format(PostData, touser,toparty,totag,agentid,media_id,title,description);
	}
	
	/**
	 * file��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��file
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param media_id ý����Դ�ļ�ID
	 * @param safe ��ʾ�Ƿ��Ǳ�����Ϣ��0��ʾ��1��ʾ�ǣ�Ĭ��0
	 * */
	public static String SFileMsg(String touser,String toparty,String totag,String agentid ,String media_id){
		String PostData = "{\"touser\": %s,\"toparty\": %s,\"totag\": %s,\"msgtype\": \"file\",\"agentid\": %s,\"file\": {\"media_id\": %s},\"safe\":\"0\"}";
		return String.format(PostData, touser,toparty,totag,agentid,media_id);
	}
	
	/**
	 * news��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��news
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param articlesList ͼ�ļ���
	 */
	public static String SNewsMsg(String touser,String toparty,String totag,String agentid , String articlesList){
		String postData = "{\"touser\": %s,\"toparty\": %s,\"totag\": %s,\"msgtype\": \"news\",\"agentid\": %s,\"news\": {\"articles\":%s}}";
		return String.format(postData, touser,toparty,totag,agentid,articlesList);
	}
	
	/**
	 * mpnews��Ϣ
	 * @param touser UserID�б���Ϣ�����ߣ�����������á�|���ָ��������������ָ��Ϊ@all�������ע����ҵӦ�õ�ȫ����Ա���͡�������"touser": "UserID1|UserID2|UserID3"
	 * @param toparty PartyID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"toparty": " PartyID1 | PartyID2 "
	 * @param totag TagID�б�����������á�|���ָ�����touserΪ@allʱ���Ա�������������"totag": " TagID1 | TagID2 "
	 * @param msgtype ��Ϣ���ͣ���ʱ�̶�Ϊ��mpnews
	 * @param agentid ��ҵӦ�õ�id�����͡�����Ӧ�õ�����ҳ��鿴
	 * @param articlesList mpnews����
	 */
	public static String SMpNewsMsg(String touser,String toparty,String totag,String agentid , String articlesList){
		String postData = "{\"touser\": %s,\"toparty\": %s,\"totag\": %s,\"msgtype\": \"mpnews\",\"agentid\": %s,\"mpnews\": {\"articles\":%s}\"safe\":\"0\"}";
		return String.format(postData, touser,toparty,totag,agentid,articlesList);
	}
	//ʾ��
   public static void main(String[] args) {
	   /**
	    * newsʾ��
	    * */
	   // ��ȡƾ֤
	   String access_token = WeixinUtil.getAccessToken(ParamesAPI.corpId, ParamesAPI.secret).getToken();
	   // �½�ͼ��
	   Article article1 = new Article();
	   article1.setTitle("news��Ϣ����-1");
	   article1.setDescription("");
	   article1.setPicUrl("http://112.124.111.3/weixinClient/images/weather3.png");
	   article1.setUrl("http://112.124.111.3/weixinClient/images/weather3.png");
	   Article article2 = new Article();
	   article2.setTitle("news��Ϣ����-2");
	   article2.setDescription("");
	   article2.setPicUrl("http://112.124.111.3/weixinClient/images/weather3.png");
	   article2.setUrl("http://112.124.111.3/weixinClient/images/weather3.png");
	   // ����ͼ��
	   List<Article> list = new ArrayList<Article>();
	   list.add(article1);
	   list.add(article2);
	   // ͼ��תjson
	   String articlesList = JSONArray.fromObject(list).toString();
	   // Post������
	   String PostData = SNewsMsg("UserID1|UserID2|UserID3", "PartyID1 | PartyID2", "TagID1 | TagID2", "1", articlesList);
	   int result = WeixinUtil.PostMessage(access_token, "POST", POST_URL, PostData);
	   // ��ӡ���
		if(0==result){
			System.out.println("�����ɹ�");
		}
		else {
			System.out.println("����ʧ��");
		}
}
}
