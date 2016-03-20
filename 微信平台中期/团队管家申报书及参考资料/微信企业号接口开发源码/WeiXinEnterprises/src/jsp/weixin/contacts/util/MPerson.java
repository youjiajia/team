package jsp.weixin.contacts.util;

import jsp.weixin.ParamesAPI.util.ParamesAPI;
import jsp.weixin.ParamesAPI.util.WeixinUtil;

/**
 * ͨѶ¼��Ա������
 * @author Engineer.Jsp
 * @date 2014.10.10*/
public class MPerson {
	//������Ա��ַ
	public static String CREATE_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN";
	//���³�Ա��ַ
	public static String UPDATA_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN";
	//ɾ����Ա��ַ
	public static String DELETE_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=ID";
	//��ȡ��Ա��ַ
	public static String GET_PERSON_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=ID";
	//��ȡ���ų�Ա��ַ
	public static String GET_GROUP_URL = "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=ACCESS_TOKEN&department_id=ID&fetch_child=0&status=0";
	
	/**
	 * ������Ա
	 * @param userid Ա��UserID����Ӧ����˵��ʺţ���ҵ�ڱ���Ψһ������Ϊ1~64���ַ�
	 * @param name ��Ա���ơ�����Ϊ1~64���ַ�
	 * @param department ��Ա��������id�б� ��ʽ�� "department": [x, y]
	 * @param position ְλ��Ϣ
	 * @param mobile �ֻ����롣��ҵ�ڱ���Ψһ��mobile/weixinid/email���߲���ͬʱΪ��
	 * @param gender �Ա�gender=0��ʾ�У�=1��ʾŮ��Ĭ��gender=0
	 * @param tel �칫�绰������Ϊ0~64���ַ�
	 * @param email ���䡣����Ϊ0~64���ַ�����ҵ�ڱ���Ψһ
	 * @param weixinid ΢�źš���ҵ�ڱ���Ψһ
	 * */
	public static String Create(String  userid,String name ,String position ,String mobile ,String gender,String tel ,String email,String weixinid){
		String PostData = "{\"userid\": %s,\"name\": %s,\"department\": [1, 2],\"position\": %s,\"mobile\": %s,\"gender\": %s,\"tel\": %s,\"email\": %s,\"weixinid\": %s}";
		return String.format(PostData, userid,name,position,mobile,gender,tel,email,weixinid);
	}
	
	/**
	 * ���³�Ա
	 * @param userid Ա��UserID����Ӧ����˵��ʺţ���ҵ�ڱ���Ψһ������Ϊ1~64���ַ�
	 * @param name ��Ա���ơ�����Ϊ1~64���ַ�
	 * @param department ��Ա��������id�б� ��ʽ�� "department": [x]
	 * @param position ְλ��Ϣ
	 * @param mobile �ֻ����롣��ҵ�ڱ���Ψһ��mobile/weixinid/email���߲���ͬʱΪ��
	 * @param gender �Ա�gender=0��ʾ�У�=1��ʾŮ��Ĭ��gender=0
	 * @param tel �칫�绰������Ϊ0~64���ַ�
	 * @param email ���䡣����Ϊ0~64���ַ�����ҵ�ڱ���Ψһ
	 * @param weixinid ΢�źš���ҵ�ڱ���Ψһ
	 * @param enable ����/���ó�Ա��1��ʾ���ó�Ա��0��ʾ���ó�Ա
	 * */
	public static String Updata(String  userid,String name ,String position ,String mobile ,String gender,String tel ,String email,String weixinid,String enable){
		String PostData = "{\"userid\": %s,\"name\": %s,\"department\": [1],\"position\": %s,\"mobile\": %s,\"gender\": %s,\"tel\": %s,\"email\": %s,\"weixinid\": %s,\"enable\": %s}";
		return String.format(PostData, userid,name,position,mobile,gender,tel,email,weixinid,enable);
	}
	
	/**
	 * ɾ����Ա
	 * @param userid Ա��UserID����Ӧ����˵��ʺ�
	 * */
	public static String Delete(String userid){
		String delete_url = DELETE_URL.replace("ID", userid);
		return delete_url;
	}
	/**
	 * ��ȡ��Ա
	 * @param userid Ա��UserID����Ӧ����˵��ʺ�
	 * */
	public static String GPerson(String userid){
		String getperson_url = GET_PERSON_URL.replace("ID", userid);
		return getperson_url;
	}
	/**
	 * ��ȡ���ų�Ա
	 * @param department_id ��ȡ�Ĳ���id
	 * @param fetch_child 1/0���Ƿ�ݹ��ȡ�Ӳ�������ĳ�Ա ����ѡ��
	 * @param status 0��ȡȫ��Ա����1��ȡ�ѹ�ע��Ա�б�2��ȡ���ó�Ա�б�4��ȡδ��ע��Ա�б�status�ɵ��� ����ѡ��
	 * */
	public static String GGroup(String department_id){
		String getgroup_url = GET_GROUP_URL.replace("ID", department_id);
		return getgroup_url;
	}
	//ʾ��
	public static void main(String[] args) {
		/**
		 * ������Աʾ��
		 * */
		// ��ȡƾ֤
		String access_token = WeixinUtil.getAccessToken(ParamesAPI.corpId, ParamesAPI.secret).getToken();
		// ƴװ����
		String PostData = Create("Ա��UserID", "Engineer-JSP", "�ܹ�ʦ", "150xxxx8524", "0", "0731-80xxx89", "jspping@qq.com", "oYxxxxxxxxxxxxxxx26336o3");
		// �ύ���ݣ���ȡ���
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
