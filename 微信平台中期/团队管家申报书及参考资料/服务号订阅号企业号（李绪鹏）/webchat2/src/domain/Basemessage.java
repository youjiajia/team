package domain;

public abstract class Basemessage {
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
		 * 返回消息类型：图文
		 */
		public static final String RESP_MESSAGE_TYPE_NEWS = "news";

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
