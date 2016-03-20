package domain.req;

import domain.BaseMessageOrEvent;

/**
 * 消息基类（企业用户-> 公众帐号）
 * @author 李绪鹏 
 * @date 2014-10-25 
 * <xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName> 
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[text]]></MsgType>
   <MsgId>1234567890123456</MsgId>
   <AgentID>1</AgentID>
 */
public abstract class Req_BaseMessage extends BaseMessageOrEvent{
	
	// 消息id，64位整型
	private long msgId;
	// 企业应用的id，整型。可在应用的设置页面查看
	private Integer agentID;
	public long getMsgId() {
		return msgId;
	}

	public void setMsgId(long msgId) {
		this.msgId = msgId;
	}

	public Integer getAgentID() {
		return agentID;
	}

	public void setAgentID(Integer agentID) {
		this.agentID = agentID;
	}

	
	
}
