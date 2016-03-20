package domain.event;

/**
 * 上报地理位置事件
 * 
 * @author 李绪鹏
 * 
 *         <xml> <ToUserName><![CDATA[toUser]]></ToUserName>
 *         <FromUserName><![CDATA[FromUser]]></FromUserName>
 *         <CreateTime>123456789</CreateTime>
 *         <MsgType><![CDATA[event]]></MsgType>
 *         <Event><![CDATA[LOCATION]]></Event> <Latitude>23.104105</Latitude>
 *         <Longitude>113.320107</Longitude> <Precision>65.000000</Precision>
 *         <AgentID>1</AgentID> </xml>
 */

public class LocationEvent extends BaseEvent {

	private String latitude;
	private String longitude;
	private String precision;

	public LocationEvent() {
		super();
		this.setMsgType(EVENT_TYPE_LOCATION);
	}

	public String getLatitude() {
		return latitude;
	}

	public void setLatitude(String latitude) {
		this.latitude = latitude;
	}

	public String getLongitude() {
		return longitude;
	}

	public void setLongitude(String longitude) {
		this.longitude = longitude;
	}

	public String getPrecision() {
		return precision;
	}

	public void setPrecision(String precision) {
		this.precision = precision;
	}

}