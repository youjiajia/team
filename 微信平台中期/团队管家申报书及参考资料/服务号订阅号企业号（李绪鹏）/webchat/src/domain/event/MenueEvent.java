package domain.event;
/**
 * 上报菜单事件
 * 点击菜单拉取消息的事件推送 CLICK 
 * 点击菜单跳转链接的事件推送 VIEW 
 * @author 李绪鹏
 * @date 2014-10-25
 *
 *<xml>
<ToUserName><![CDATA[toUser]]></ToUserName>
<FromUserName><![CDATA[FromUser]]></FromUserName>
<CreateTime>123456789</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[CLICK]]></Event>
<EventKey><![CDATA[EVENTKEY]]></EventKey>
<AgentID>1</AgentID>
</xml>
 */

public class MenueEvent extends BaseEvent {
	/**
	 *CLICK 事件KEY值，与自定义菜单接口中KEY值对应 
	 * VIEW	事件KEY值，设置的跳转URL 
	 */
	private  String eventKey;

	public String getEventKey() {
		return eventKey;
	}

	public void setEventKey(String eventKey) {
		this.eventKey = eventKey;
	}
	
	
}
