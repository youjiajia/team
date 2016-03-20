package domain.req;

/**
 * 文本消息
 * 
 *@author 李绪鹏 
 *@date 2014-10-25 
 *<xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName> 
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[text]]></MsgType>
   <Content><![CDATA[this is a test]]></Content>
   <MsgId>1234567890123456</MsgId>
   <AgentID>1</AgentID>
</xml>
 */
public class Req_TextMessage extends Req_BaseMessage {
	// 文本消息内容 
	private String content;
	

	public Req_TextMessage() {
		super();
		this.setMsgType(REQ_MESSAGE_TYPE_TEXT);
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}	
}