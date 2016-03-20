package jsp.weixin.contacts.util;

import jsp.weixin.ParamesAPI.util.ParamesAPI;
import jsp.weixin.ParamesAPI.util.WeixinUtil;

/**
 * ͨѶ¼��ǩ������
 * @author Engineer.Jsp
 * @date 2014.10.10*/
public class MTag {
	//������ǩ��ַ
	public static String CREATE_TAG_URL = "https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN";
	//���±�ǩ��ַ
	public static String UPDATA_TAG_URL = "https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN";
	//ɾ����ǩ��ַ
	public static String DELETE_TAG_URL = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=ID";
	//��ȡ��ǩ��Ա��ַ
	public static String GET_TAG_PERSON = "https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=ID";
	//���ӱ�ǩ��Ա��ַ
	public static String ADD_TAG_PERSON = "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=ACCESS_TOKEN";
	//ɾ����ǩ��Ա��ַ
	public static String DELETE_TAG_PERSON = "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token=ACCESS_TOKEN";
	
	
	/**
	 * ������ǩ
	 * @param tagname ��ǩ���ơ�����Ϊ1~64���ַ�����ǩ����������ͬ��ı�ǩ������Ҳ������ȫ�ֱ�ǩ����
	 * */
	public static String Create_Tag(String tagname){
		String PostData = "{\"tagname\": %s}";
		return String.format(PostData, tagname);
	}
	
	/**
	 * ���±�ǩ����
	 * @param tagid ��ǩID
	 * @param tagname ��ǩ���ơ��64���ַ�
	 * */
	public static String Updata_Tag(String tagid , String tagname){
		String PostData = "{\"tagid\": %s,\"tagname\": %s}";
		return String.format(PostData, tagid,tagname);
	}
	
	/**
	 * ɾ����ǩ
	 * @param tagid ��ǩID
	 * */
	public static String Delete_Tag(String tagid){
		String delete_url = DELETE_TAG_URL.replace("ID", tagid);
		return delete_url;
	}
	
	/**
	 * ��ȡ��ǩ��Ա
	 * @param tagid ��ǩID
	 * */
	public static String Get_Tag_Person(String tagid){
		String get_tagperson_url = GET_TAG_PERSON.replace("ID", tagid);
		return get_tagperson_url;
	}
	
	/**
	 * ���ӱ�ǩ��Ա
	 * @param tagid ��ǩID
	 * @param userlist ��ҵԱ��ID�б� ��ʽ��"userlist":[ "user1","user2"]
	 * */
	public static String Add_Tag_Person(String tagid,String userlist){
		String PostData = "{\"tagid\": %s,\"userlist\":%s}";
		return String.format(PostData, tagid,userlist);
	}
	
	/**
	 * ɾ����ǩ��Ա
	 * @param tagid ��ǩID
	 * @param userlist ��ҵԱ��ID�б� ��ʽ��"userlist":[ "user1","user2"]
	 * */
	public static String Delete_Tag_Person(String tagid,String userlist){
		String PostData = "{\"tagid\": %s,\"userlist\":%s}";
		return String.format(PostData, tagid,userlist);
	}
	//ʾ��
	public static void main(String[] args) {
		/**
		 * ������ǩʾ��
		 * */
		// ��ȡƾ֤
		String access_token = WeixinUtil.getAccessToken(ParamesAPI.corpId, ParamesAPI.secret).getToken();
		// ƴװ����
		String PostData = Create_Tag("�½���ǩ");
		// �ύ���ݣ���ȡ���
		int result = WeixinUtil.PostMessage(access_token, "POST", CREATE_TAG_URL, PostData);
		// ��ӡ���
		if(0==result){
			System.out.println("�����ɹ�");
		}
		else {
			System.out.println("����ʧ��");
		}
	}

}
