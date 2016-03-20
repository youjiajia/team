package domain.resp;

import domain.Video;

/**
 * 视频model
 * @author 李绪鹏
 * @date 2014-10-25
 *<xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>1357290913</CreateTime>
   <MsgType><![CDATA[video]]></MsgType>
   <Video>
       <MediaId><![CDATA[media_id]]></MediaId>
       <Title><![CDATA[title]]></Title>
       <Description><![CDATA[description]]></Description>
   </Video>
</xml>
 */
public class Resp_VideoMessage extends Resp_BaseMessage {
	//视频
	private Video video;

	public Video getVideo() {
		return video;
	}

	public void setVideo(Video video) {
		this.video = video;
	}
	

}
