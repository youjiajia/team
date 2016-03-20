package domain.resp;

import domain.Voice;

/**
 * 
 * 回复语言信息
 * @author 李绪鹏
 * @date 2014-10-25
 *<xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>1357290913</CreateTime>
   <MsgType><![CDATA[voice]]></MsgType>
   <Voice>
       <MediaId><![CDATA[media_id]]></MediaId>
   </Voice>
</xml>
 */
public class Resp_VoiceMessage extends Resp_BaseMessage {
	
	//语音
	private Voice voice;

	public Resp_VoiceMessage() {
		super();
		this.setMsgType("voice");
	}

	public Voice getVoice() {
		return voice;
	}

	public void setVoice(Voice voice) {
		this.voice = voice;
	}
	

}
