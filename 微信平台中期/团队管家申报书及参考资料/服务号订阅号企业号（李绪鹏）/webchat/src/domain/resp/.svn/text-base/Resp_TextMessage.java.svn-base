package domain.resp;

/**
 * 文本消息
 * 
 * @author 李绪鹏
 * @date 2014-10-25
 *
 *<xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName> 
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[text]]></MsgType>
   <Content><![CDATA[this is a test]]></Content>
</xml>
*/
public class Resp_TextMessage extends Resp_BaseMessage {
	// 回复的消息内容
	private String content;

	public Resp_TextMessage() {
		super();
		this.setMsgType(RESP_MESSAGE_TYPE_TEXT);
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}
}