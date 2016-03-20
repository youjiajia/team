package domain.event;

import domain.BaseMessageOrEvent;
/**
 * 事件的基类
 * @author 李绪鹏
 * @date 2014-10-25
 *<xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[UserID]]></FromUserName>
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[event]]></MsgType>
   <Event><![CDATA[subscribe]]></Event>
   <AgentID>1</AgentID>
</xml>
 */


public abstract class BaseEvent extends BaseMessageOrEvent{
	//事件类型，此时固定为
	private String event;
	public BaseEvent() {
		super();
		this.setMsgType(REQ_MESSAGE_TYPE_EVENT);
	}
	// 	企业应用的id，整型。可在应用的设置页面获取；如果id为0，则表示是整个企业号的关注/取消关注事件 
	private String agentId;
	public String getEvent() {
		return event;
	}
	public void setEvent(String event) {
		this.event = event;
	}
	public String getAgentId() {
		return agentId;
	}
	public void setAgentId(String agentId) {
		this.agentId = agentId;
	}


}
