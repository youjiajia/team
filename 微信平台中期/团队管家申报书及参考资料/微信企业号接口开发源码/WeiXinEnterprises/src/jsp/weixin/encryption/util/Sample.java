package jsp.weixin.encryption.util;

//
//import java.io.StringReader;
//
//import javax.xml.parsers.DocumentBuilder;
//import javax.xml.parsers.DocumentBuilderFactory;
//
//import org.w3c.dom.Document;
//import org.w3c.dom.Element;
//import org.w3c.dom.NodeList;
//import org.xml.sax.InputSource;

public class Sample {

	public static void main(String[] args) throws Exception {
		String sToken = "wanchuang";
		String sCorpID = "wx951606f0932ebe1f";
		String sEncodingAESKey = "zLsSe7zIquAxb2nK9Dpe4nJP4E1r5L17Fe5Apn1Dmtt";

		WXBizMsgCrypt wxcpt = new WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID);
		/*
		 * �ٶ�����ƽ̨�Ͽ��������õ�Token 1. ��֤�ص�URL �����֤ʱ����ҵ�յ��������� GET
		 * /cgi-bin/wxpush?msg_signature
		 * =5c45ff5e21c57e6ad56bac8758b79b1d9ac89fd3
		 * &timestamp=1409659589&nonce=263014780
		 * &echostr=P9nAzCzyDtyTWESHep1vC5X9xho
		 * %2FqYX3Zpb4yKa9SKld1DsH3Iyt3tP3zNdtp
		 * %2B4RPcs8TgAE7OaBO%2BFZXvnaqQ%3D%3D HTTP/1.1 Host: qy.weixin.qq.com
		 * ���յ�������ʱ����ҵӦ1.����֤ǩ������ȷ�� 2. ���ܳ�echostrԭ�ġ� ����������VerifyURL���
		 */
		// ������url�ϵĲ���ֵ���£�
		String sVerifyMsgSig = "86aaf5f5d99ef7867e706c249e1b75d473aa4978";
		String sVerifyTimeStamp = "1411523034";
		String sVerifyNonce = "1922577216";
		String sVerifyEchoStr = "HzMGxeddC9%2BGwFH%2FdmLjtVOlbTnCCaDJe4P4cMYUMZ5grHqxpRV6UZWkT2ZibD7xzm0rh9uH2FLxyC0I7vGDoA%3D%3D";
		String sEchoStr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce,
				sVerifyEchoStr);
		System.out.println("verifyurl echostr: " + sEchoStr);

		/*
		 * 2. ���û��ظ������ݽ��н��ܡ� �û��ظ���Ϣ���ߵ���¼���Ӧʱ����ҵ���յ��ص���Ϣ��������ҵ�յ���������Ϣ�� POST
		 * /cgi-bin/wxpush?
		 * msg_signature=477715d11cdb4164915debcba66cb864d751f3e6
		 * &timestamp=1409659813&nonce=1372623149 HTTP/1.1 Host:
		 * qy.weixin.qq.com Content-Length: 613
		 * 
		 * <xml> <ToUserName><![CDATA[wx5823bf96d3bd56c7]]></ToUserName>
		 * <Encrypt><![CDATA[RypEvHKD8QQKFhvQ6QleEB4J58tiPdvo+rtK1I9qca6aM/
		 * wvqnLSV5zEPeusUiX5L5X/0lWfrf0QADHHhGd3QczcdCUpj911L3vg3W/
		 * sYYvuJTs3TUUkSUXxaccAS0qhxchrRYt66wiSpGLYL42aM6A8dTT
		 * +6k4aSknmPj48kzJs8qLjvd4Xgpue06DOdnLxAUHzM6
		 * +kDZ+HMZfJYuR+LtwGc2hgf5gsijff0ekUNXZiqATP7PF5mZxZ3Izoun1s4zG4LUMnvw2r
		 * +KqCKIw+3IQH03v+
		 * BCA9nMELNqbSf6tiWSrXJB3LAVGUcallcrw8V2t9EL4EhzJWrQUax5wLVMNS0
		 * +rUPA3k22Ncx4XXZS9o0MBH27Bo6BpNelZpS
		 * +/uh9KsNlY6bHCmJU9p8g7m3fVKn28H3KDYA5Pl
		 * /T8Z1ptDAVe0lXdQ2YoyyH2uyPIGHBZZIs2pDBS8R07+qN+E7Q==]]></Encrypt>
		 * <AgentID><![CDATA[218]]></AgentID> </xml>
		 */
		String sReqMsgSig = "477715d11cdb4164915debcba66cb864d751f3e6";
		String sReqTimeStamp = "1409659813";
		String sReqNonce = "1372623149";
		String sReqData = "<xml><ToUserName><![CDATA[wx5823bf96d3bd56c7]]></ToUserName><Encrypt><![CDATA[RypEvHKD8QQKFhvQ6QleEB4J58tiPdvo+rtK1I9qca6aM/wvqnLSV5zEPeusUiX5L5X/0lWfrf0QADHHhGd3QczcdCUpj911L3vg3W/sYYvuJTs3TUUkSUXxaccAS0qhxchrRYt66wiSpGLYL42aM6A8dTT+6k4aSknmPj48kzJs8qLjvd4Xgpue06DOdnLxAUHzM6+kDZ+HMZfJYuR+LtwGc2hgf5gsijff0ekUNXZiqATP7PF5mZxZ3Izoun1s4zG4LUMnvw2r+KqCKIw+3IQH03v+BCA9nMELNqbSf6tiWSrXJB3LAVGUcallcrw8V2t9EL4EhzJWrQUax5wLVMNS0+rUPA3k22Ncx4XXZS9o0MBH27Bo6BpNelZpS+/uh9KsNlY6bHCmJU9p8g7m3fVKn28H3KDYA5Pl/T8Z1ptDAVe0lXdQ2YoyyH2uyPIGHBZZIs2pDBS8R07+qN+E7Q==]]></Encrypt><AgentID><![CDATA[218]]></AgentID></xml>";

		String sMsg = wxcpt.DecryptMsg(sReqMsgSig, sReqTimeStamp, sReqNonce, sReqData);
		System.out.println("after decrypt msg: " + sMsg);

		/*
		 * 3. ��ҵ�ظ��û���ϢҲ��Ҫ���ܺ�ƴ��xml�ַ����� ������ҵ��Ҫ�ظ��û�����ϢΪ�� <xml>
		 * <ToUserName><![CDATA[mycreate]]></ToUserName>
		 * <FromUserName><![CDATA[wx5823bf96d3bd56c7]]></FromUserName>
		 * <CreateTime>1348831860</CreateTime>
		 * <MsgType><![CDATA[text]]></MsgType> <Content><![CDATA[this is a
		 * test]]></Content> <MsgId>1234567890123456</MsgId>
		 * <AgentID>128</AgentID> </xml> ����xml��ʽ�ļ�����Ϣ����Ϊ��
		 */
		String sRespData = "<xml><ToUserName><![CDATA[mycreate]]></ToUserName><FromUserName><![CDATA[wx5823bf96d3bd56c7]]></FromUserName><CreateTime>1348831860</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[this is a test]]></Content><MsgId>1234567890123456</MsgId><AgentID>128</AgentID></xml>";

		String sEncryptMsg = wxcpt.EncryptMsg(sRespData, sReqTimeStamp, sReqNonce);
		System.out.println("after encrypt sEncrytMsg: " + sEncryptMsg);

	}
}
