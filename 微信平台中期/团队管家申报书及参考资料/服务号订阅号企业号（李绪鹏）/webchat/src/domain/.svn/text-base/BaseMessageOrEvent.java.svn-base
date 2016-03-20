package domain;

public abstract class BaseMessageOrEvent {
	// 企业号CorpID
		private String toUserName;
		// 员工UserID
		private String fromUserName;
		// 消息创建时间（整型）
		private long createTime;
		// 消息类型，此时固定为（text/image/location/link）
		private String msgType;
		/**
		 * 返回消息类型：文本
		 */
		public static final String RESP_MESSAGE_TYPE_TEXT = "text";

		/**
		 * 返回消息类型：音乐
		 */
		public static final String RESP_MESSAGE_TYPE_MUSIC = "music";
		/**
		 * 返回消息类型：视频
		 */
		public static final String RESP_MESSAGE_TYPE_VIDEO = "video";

		/**
		 * 返回消息类型：图文
		 */
		public static final String RESP_MESSAGE_TYPE_NEWS = "news";
		/**
		 * 返回消息类型：音频
		 */
		public static final String RESP_MESSAGE_TYPE_VOICE = "voice";

		/**
		 * 请求消息类型：文本
		 */
		public static final String REQ_MESSAGE_TYPE_TEXT = "text";

		/**
		 * 请求消息类型：图片
		 */
		public static final String REQ_MESSAGE_TYPE_IMAGE = "image";

		/**
		 * 请求消息类型：链接
		 */
		public static final String REQ_MESSAGE_TYPE_LINK = "link";

		/**
		 * 请求消息类型：地理位置
		 */
		public static final String REQ_MESSAGE_TYPE_LOCATION = "location";

		/**
		 * 请求消息类型：音频
		 */
		public static final String REQ_MESSAGE_TYPE_VOICE = "voice";

		/**
		 * 请求消息类型：推送
		 */
		public static final String REQ_MESSAGE_TYPE_EVENT = "event";

		/**
		 * 事件类型：subscribe(订阅)
		 */
		public static final String EVENT_TYPE_SUBSCRIBE = "subscribe";

		/**
		 * 事件类型：unsubscribe(取消订阅)
		 */
		public static final String EVENT_TYPE_UNSUBSCRIBE = "unsubscribe";

		/**
		 * 事件类型：CLICK(自定义菜单点击事件)
		 */
		public static final String EVENT_TYPE_CLICK = "CLICK";
		public static final String EVENT_TYPE_LOCATION = "LOCATION";
		public static final String EVENT_TYPE_VIEW  = "VIEW";
		public static final String EVENT_TYPE_SCANCODE_PUSH = "scancode_push";
		public static final String EVENT_TYPE_PIC_SYSPHOTO = "pic_sysphoto";
		public static final String EVENT_TYPE_PIC_PHOTO_OR_ALBUM= "pic_photo_or_album ";

		public String getToUserName() {
			return toUserName;
		}

		public void setToUserName(String toUserName) {
			this.toUserName = toUserName;
		}

		public String getFromUserName() {
			return fromUserName;
		}

		public void setFromUserName(String fromUserName) {
			this.fromUserName = fromUserName;
		}

		public long getCreateTime() {
			return createTime;
		}

		public void setCreateTime(long createTime) {
			this.createTime = createTime;
		}

		public String getMsgType() {
			return msgType;
		}

		public void setMsgType(String msgType) {
			this.msgType = msgType;
		}

}
