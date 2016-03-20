package domain.resp;

import domain.Image;

/**
 * 图片model
 * 
 * @author 李绪鹏
 * @date 2014-10-25
 * <xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>1348831860</CreateTime>
   <MsgType><![CDATA[image]]></MsgType>
   <Image>
       <MediaId><![CDATA[media_id]]></MediaId>
   </Image>
</xml>
 */
public class Resp_ImeageMessage extends Resp_BaseMessage {
	
	//图片
	private Image image;
	
	public Resp_ImeageMessage() {
		super();
		this.setMsgType(REQ_MESSAGE_TYPE_IMAGE);
	}
	
	public Image getImage() {
		return image;
	}
	public void setImage(Image image) {
		this.image = image;
	}

}
