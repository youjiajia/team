package jsp.weixin.contacts.util;

import jsp.weixin.ParamesAPI.util.ParamesAPI;
import jsp.weixin.ParamesAPI.util.WeixinUtil;

/**
 * ͨѶ¼���Ź�����
 * @author Engineer.Jsp
 * @date 2014.10.10*/
public class MGroup {
	
	// �������ŵ�ַ
	public static String CREATE_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN";
	// ���²��ŵ�ַ
	public static String UPDATE_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=ACCESS_TOKEN";
	// ɾ�����ŵ�ַ
	public static String DELETE_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=ACCESS_TOKEN&id=ID";
	// ��ȡ�����б��ַ
	public static String GETLIST_URL = "https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=ACCESS_TOKEN";
	
	/**
	 * ��������
	 * @param name �������ơ���������Ϊ1~64���ַ�
	 * @param parentid ���ײ���id��������idΪ1
	 * */
	public static String Create(String name , String parentid){
		String Postjson = "{\"name\": %s,\"parentid\": %s}";
		return String.format(Postjson, name,parentid);
	}
	
	/**
	 * ���²���
	 * @param name ���µĲ������ơ���������Ϊ0~64���ַ����޸Ĳ�������ʱָ���ò���
	 * @param id ����id
	 * */
	public static String Update(String name , String id){
		String Postjson = "{\"id\": %s,\"name\": %s}";
		return String.format(Postjson, name,id);
	}
	
	/**
	 * ɾ������
	 * @param id ����id
	 * */
	public static String Delete(String id){
		String delete_url = DELETE_URL.replace("ID", id);
		return delete_url;
	}
	//ʾ��
	public static void main(String[] args) {
		/**
		 * ��������ʾ��
		 * */
		// ��ȡƾ֤
		String access_token = WeixinUtil.getAccessToken(ParamesAPI.corpId, ParamesAPI.secret).getToken();
		// ƴװ����
		String PostData = Create("�½�����", "2");
		// �ύ����,��ȡ���
		int result = WeixinUtil.PostMessage(access_token, "POST", CREATE_URL, PostData);
		// ��ӡ���
		if(0==result){
			System.out.println("�����ɹ�");
		}
		else {
			System.out.println("����ʧ��");
		}
	}
}
