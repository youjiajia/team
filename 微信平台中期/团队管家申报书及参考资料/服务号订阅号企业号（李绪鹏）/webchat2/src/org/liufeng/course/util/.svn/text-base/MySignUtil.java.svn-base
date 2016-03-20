package org.liufeng.course.util;

import java.io.IOException;
import java.util.Arrays;

import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.DigestUtils;
import org.junit.Test;
/**
 * 请求校验工具类
 * 
 * @author liufeng
 * @date 2013-05-18
 */
/*@Deprecated*/
public class MySignUtil {
	// 与接口配置信息中的Token要一致
	private static String token = "weixinCourse";

	/**
	 * 验证签名
	 * 
	 * @param msg_signature
	 * @param timestamp
	 * @param nonce
	 * @param msg_encrypt
	 * @return
	 */
	public static boolean checkSignature(String msg_signature, String timestamp, String nonce,String msg_encrypt) {
		String[] arr = new String[] { token, timestamp, nonce,msg_encrypt};
		// 将token、timestamp、nonce,msg_encrypt四个参数进行字典序排序
		Arrays.sort(arr);
		StringBuilder content = new StringBuilder();
		for (int i = 0; i < arr.length; i++) {
			content.append(arr[i]);
		}
		String tmpStr = DigestUtils.shaHex(content.toString());
		content=null;
		// 将sha1加密后的字符串可与signature对比，标识该请求来源于微信
		return tmpStr != null ? tmpStr.equals(msg_signature) : false;
	}
	
	public static String decrypt4Msg_encrypt(String msg_encrypt) throws IOException
	{
		Base64.decodeBase64(msg_encrypt.getBytes());
		return null;
	}

	@Test
	public void test() throws IOException
	{
		decrypt4Msg_encrypt("msg_encrypt");
	}
	
}
