package jsp.weixin.media.util;

/**
 * ý���ļ���Ϣ
 * 
 *@author Engineer-Jsp
 *@date 2014.10.10
 */
public class WeixinMedia {
	// ý���ļ�����
	private String type;
	// ý���ļ���ʶ������ͼ��ý���ļ���ʶ
	private String mediaId;
	// ý���ļ��ϴ���ʱ��
	private int createdAt;

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getMediaId() {
		return mediaId;
	}

	public void setMediaId(String mediaId) {
		this.mediaId = mediaId;
	}

	public int getCreatedAt() {
		return createdAt;
	}

	public void setCreatedAt(int createdAt) {
		this.createdAt = createdAt;
	}
}
