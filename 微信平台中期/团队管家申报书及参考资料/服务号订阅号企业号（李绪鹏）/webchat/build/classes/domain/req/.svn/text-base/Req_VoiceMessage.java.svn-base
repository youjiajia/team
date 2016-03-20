    package domain.req;  
      
    /** 
     * 音频消息 
     *  
     * @author 李绪鹏 
     * @date 2014-10-25 
     * <xml>
   <ToUserName><![CDATA[toUser]]></ToUserName>
   <FromUserName><![CDATA[fromUser]]></FromUserName>
   <CreateTime>1357290913</CreateTime>
   <MsgType><![CDATA[voice]]></MsgType>
   <MediaId><![CDATA[media_id]]></MediaId>
   <Format><![CDATA[Format]]></Format>
   <MsgId>1234567890123456</MsgId>
   <AgentID>1</AgentID>
</xml>
     */  
    public class Req_VoiceMessage extends Req_BaseMessage {  
        // 语音媒体文件id，可以调用获取媒体文件接口拉取数据
        private String mediaId;  
        // 语音格式，如amr，speex等 
        private String format;
        
        
		public Req_VoiceMessage() {
			super();
			this.setMsgType(REQ_MESSAGE_TYPE_VOICE);
		}
		public String getMediaId() {
			return mediaId;
		}
		public void setMediaId(String mediaId) {
			this.mediaId = mediaId;
		}
		public String getFormat() {
			return format;
		}
		public void setFormat(String format) {
			this.format = format;
		}  

    }  