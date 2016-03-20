package jsp.weixin.media.util;

/**
 * ý��ӿ���
 * @author Engineer.Jsp
 * @date 2014.10.10*/
import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import jsp.weixin.ParamesAPI.util.ParamesAPI;
import jsp.weixin.ParamesAPI.util.WeixinUtil;
import net.sf.json.JSONObject;
public class MUDload {
	
	/**
	 * �ϴ�ý���ļ�
	 * @param accessToken �ӿڷ���ƾ֤
	 * @param type ý���ļ����ͣ��ֱ���ͼƬ��image����������voice������Ƶ��video������ͨ�ļ�(file)
	 * @param media form-data��ý���ļ���ʶ����filename��filelength��content-type����Ϣ
	 * @param mediaFileUrl ý���ļ���url
	 * �ϴ���ý���ļ�����
     * ͼƬ��image��:1MB��֧��JPG��ʽ
     * ������voice����2MB�����ų��Ȳ�����60s��֧��AMR��ʽ
     * ��Ƶ��video����10MB��֧��MP4��ʽ
     * ��ͨ�ļ���file����10MB
	 * */
	public static WeixinMedia uploadMedia(String accessToken, String type, String mediaFileUrl) {
		WeixinMedia weixinMedia = null;
		// ƴװ�����ַ
		String uploadMediaUrl = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=ACCESS_TOKEN&type=TYPE";
		uploadMediaUrl = uploadMediaUrl.replace("ACCESS_TOKEN", accessToken).replace("TYPE", type);

		// �������ݷָ���
		String boundary = "------------7da2e536604c8";
		try {
			URL uploadUrl = new URL(uploadMediaUrl);
			HttpURLConnection uploadConn = (HttpURLConnection) uploadUrl.openConnection();
			uploadConn.setDoOutput(true);
			uploadConn.setDoInput(true);
			uploadConn.setRequestMethod("POST");
			// ��������ͷContent-Type
			uploadConn.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);
			// ��ȡý���ļ��ϴ������������΢�ŷ�����д���ݣ�
			OutputStream outputStream = uploadConn.getOutputStream();

			URL mediaUrl = new URL(mediaFileUrl);
			HttpURLConnection meidaConn = (HttpURLConnection) mediaUrl.openConnection();
			meidaConn.setDoOutput(true);
			meidaConn.setRequestMethod("GET");

			// ������ͷ�л�ȡ��������
			String contentType = meidaConn.getHeaderField("Content-Type");
			// �������������ж��ļ���չ��
			String fileExt = WeixinUtil.getFileEndWitsh(contentType);
			// �����忪ʼ
			outputStream.write(("--" + boundary + "\r\n").getBytes());
			outputStream.write(String.format("Content-Disposition: form-data; name=\"media\"; filename=\"file1%s\"\r\n", fileExt).getBytes());
			outputStream.write(String.format("Content-Type: %s\r\n\r\n", contentType).getBytes());

			// ��ȡý���ļ�������������ȡ�ļ���
			BufferedInputStream bis = new BufferedInputStream(meidaConn.getInputStream());
			byte[] buf = new byte[8096];
			int size = 0;
			while ((size = bis.read(buf)) != -1) {
				// ��ý���ļ�д�����������΢�ŷ�����д���ݣ�
				outputStream.write(buf, 0, size);
			}
			// ���������
			outputStream.write(("\r\n--" + boundary + "--\r\n").getBytes());
			outputStream.close();
			bis.close();
			meidaConn.disconnect();

			// ��ȡý���ļ��ϴ�������������΢�ŷ����������ݣ�
			InputStream inputStream = uploadConn.getInputStream();
			InputStreamReader inputStreamReader = new InputStreamReader(inputStream, "utf-8");
			BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
			StringBuffer buffer = new StringBuffer();
			String str = null;
			while ((str = bufferedReader.readLine()) != null) {
				buffer.append(str);
			}
			bufferedReader.close();
			inputStreamReader.close();
			// �ͷ���Դ
			inputStream.close();
			inputStream = null;
			uploadConn.disconnect();

			// ʹ��JSON-lib�������ؽ��
			JSONObject jsonObject = JSONObject.fromObject(buffer.toString());
			weixinMedia = new WeixinMedia();
			weixinMedia.setType(jsonObject.getString("type"));
			// type���� ����ͼ��thumb�� ʱ�ķ��ؽ�����������Ͳ�һ��
			if ("thumb".equals(type))
				weixinMedia.setMediaId(jsonObject.getString("thumb_media_id"));
			else
				weixinMedia.setMediaId(jsonObject.getString("media_id"));
			    weixinMedia.setCreatedAt(jsonObject.getInt("created_at"));
		} catch (Exception e) {
			weixinMedia = null;
			String error = String.format("�ϴ�ý���ļ�ʧ�ܣ�%s", e);
			System.out.println(error);
		}
		return weixinMedia;
	}
	
	/**
	 * ��ȡý���ļ�
	 * @param accessToken �ӿڷ���ƾ֤
	 * @param media_id ý���ļ�id
	 * @param savePath �ļ��ڷ������ϵĴ洢·��
	 * */
	public static String downloadMedia(String accessToken, String mediaId, String savePath) {
		String filePath = null;
		// ƴ�������ַ
		String requestUrl = "https://qyapi.weixin.qq.com/cgi-bin/media/get?access_token=ACCESS_TOKEN&media_id=MEDIA_ID";
		requestUrl = requestUrl.replace("ACCESS_TOKEN", accessToken).replace("MEDIA_ID", mediaId);
		System.out.println(requestUrl);
		try {
			URL url = new URL(requestUrl);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setDoInput(true);
			conn.setRequestMethod("GET");

			if (!savePath.endsWith("/")) {
				savePath += "/";
			}
			// �����������ͻ�ȡ��չ��
			String fileExt = WeixinUtil.getFileEndWitsh(conn.getHeaderField("Content-Type"));
			// ��mediaId��Ϊ�ļ���
			filePath = savePath + mediaId + fileExt;

			BufferedInputStream bis = new BufferedInputStream(conn.getInputStream());
			FileOutputStream fos = new FileOutputStream(new File(filePath));
			byte[] buf = new byte[8096];
			int size = 0;
			while ((size = bis.read(buf)) != -1)
				fos.write(buf, 0, size);
			fos.close();
			bis.close();

			conn.disconnect();
			String info = String.format("����ý���ļ��ɹ���filePath=" + filePath);
			System.out.println(info);
		} catch (Exception e) {
			filePath = null;
			String error = String.format("����ý���ļ�ʧ�ܣ�%s", e);
			System.out.println(error);
		}
		return filePath;
	}
    //ʾ��
	public static void main(String[] args) {
		/**
		 * �ϴ���ý���ļ�
		 */
		String access_token = WeixinUtil.getAccessToken(ParamesAPI.corpId, ParamesAPI.secret).getToken();
		//��ַ
		WeixinMedia weixinMedia = uploadMedia(access_token, "image", "http://localhost:8080/weixinClient/weather1.jpg");
		//media_id
		System.out.println(weixinMedia.getMediaId());
		//����
		System.out.println(weixinMedia.getType());
		//ʱ���
		System.out.println(weixinMedia.getCreatedAt());
		//��ӡ���
		if(null!=weixinMedia){
			System.out.println("�ϴ��ɹ���");
		}else{
			System.out.println("�ϴ�ʧ�ܣ�");
		}

	}

}
