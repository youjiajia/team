package domain.req;

/**
 * 地理位置消息
 * 
 * @author 李绪鹏
 * @date 2014-10-25
 * <xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>1351776360</CreateTime>
   <MsgType><![CDATA[location]]></MsgType>
   <Location_X>23.134521</Location_X>
   <Location_Y>113.358803</Location_Y>
   <Scale>20</Scale>
   <Label><![CDATA[位置信息]]></Label>
   <MsgId>1234567890123456</MsgId>
   <AgentID>1</AgentID>
</xml>
 */
public class Req_LocationMessage extends Req_BaseMessage {
	// 地理位置维度
	private String location_X;
	// 地理位置经度
	private String location_Y;
	// 地图缩放大小
	private String scale;
	// 地理位置信息
	private String sabel;
	
	public Req_LocationMessage() {
		super();
		this.setMsgType(REQ_MESSAGE_TYPE_LOCATION);
	}
	public String getLocation_X() {
		return location_X;
	}
	public void setLocation_X(String location_X) {
		this.location_X = location_X;
	}
	public String getLocation_Y() {
		return location_Y;
	}
	public void setLocation_Y(String location_Y) {
		this.location_Y = location_Y;
	}
	public String getScale() {
		return scale;
	}
	public void setScale(String scale) {
		this.scale = scale;
	}
	public String getSabel() {
		return sabel;
	}
	public void setSabel(String sabel) {
		this.sabel = sabel;
	}
}