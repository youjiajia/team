package domain.req;

/**
 * 图片消息
 * 
 * @author 李绪鹏 
 * @date 2014-10-25 
 * <xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[image]]></MsgType>
   <PicUrl><![CDATA[this is a url]]></PicUrl>
   <MediaId><![CDATA[media_id]]></MediaId>
   <MsgId>1234567890123456</MsgId>
   <AgentID>1</AgentID>
</xml>
 */
public class Req_ImageMessage extends Req_BaseMessage {
	// 图片链接
	private String picUrl;
	//图片媒体文件id，可以调用获取媒体文件接口拉取数据 
	private String mediaId;
	
	
	public Req_ImageMessage() {
		super();
		this.setMsgType(REQ_MESSAGE_TYPE_IMAGE);
	}
	public String getPicUrl() {
		return picUrl;
	}
	public void setPicUrl(String picUrl) {
		this.picUrl = picUrl;
	}
	public String getMediaId() {
		return mediaId;
	}
	public void setMediaId(String mediaId) {
		this.mediaId = mediaId;
	}
}
