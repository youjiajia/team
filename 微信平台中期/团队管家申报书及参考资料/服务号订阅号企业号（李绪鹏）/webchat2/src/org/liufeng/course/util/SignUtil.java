package org.liufeng.course.util;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;

import org.apache.commons.codec.digest.DigestUtils;
import org.junit.Test;

/**
 * 请求校验工具类
 * 
 * @author liufeng
 * @date 2013-05-18
 */
@Deprecated
public class SignUtil {
	// 与接口配置信息中的Token要一致
	private static String token = "weixinCourse";

	/**
	 * 验证签名
	 * 
	 * @param signature
	 * @param timestamp
	 * @param nonce
	 * @return
	 */
	public static boolean checkSignature(String signature, String timestamp, String nonce) {
		String[] arr = new String[] { token, timestamp, nonce };
		// 将token、timestamp、nonce三个参数进行字典序排序
		Arrays.sort(arr);
		StringBuilder content = new StringBuilder();
		for (int i = 0; i < arr.length; i++) {
			content.append(arr[i]);
		}
		MessageDigest md = null;
		String tmpStr = null;

		try {
			md = MessageDigest.getInstance("SHA-1");
			// 将三个参数字符串拼接成一个字符串进行sha1加密
			byte[] digest = md.digest(content.toString().getBytes());
			tmpStr = byteToStr(digest);
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}

		content = null;
		// 将sha1加密后的字符串可与signature对比，标识该请求来源于微信
		return tmpStr != null ? tmpStr.equals(signature.toUpperCase()) : false;
	}

	/**
	 * 将字节数组转换为十六进制字符串
	 * 
	 * @param byteArray
	 * @return
	 */
	private static String byteToStr(byte[] byteArray) {
		String strDigest = "";
		for (int i = 0; i < byteArray.length; i++) {
			strDigest += byteToHexStr(byteArray[i]);
		}
		return strDigest;
	}

	/**
	 * 将字节转换为十六进制字符串
	 * 
	 * @param mByte
	 * @return
	 */
	private static String byteToHexStr(byte mByte) {
		char[] Digit = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };
		char[] tempArr = new char[2];
		tempArr[0] = Digit[(mByte >>> 4) & 0X0F];
		tempArr[1] = Digit[mByte & 0X0F];

		String s = new String(tempArr);
		return s;
	}
	/**我用框架和柳峰shal的生成的做对比，
	 * 这个方法只是做测试用
	 * 
	 * @author 李绪鹏
	 * @throws UnsupportedEncodingException 
	 */
	@Test
	public void testDigest() throws UnsupportedEncodingException
	{
		MessageDigest md = null;
		String tmpStr = null;
	String string="aaaaaaaaa";
	try {
		md = MessageDigest.getInstance("SHA-1");
	} catch (NoSuchAlgorithmException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	// 将三个参数字符串拼接成一个字符串进行sha1加密
	byte[] digest = md.digest(string.toString().getBytes());
	tmpStr = byteToStr(digest);
	System.out.println(tmpStr);
	System.out.println(DigestUtils.shaHex(string));
	System.out.println(URLEncoder.encode("中国","utf-8"));
	System.out.println(URLEncoder.encode("a","utf-8"));
	System.out.println(URLDecoder.decode("%E4%B8%AD%E5%9B%BD","utf-8"));
	System.out.println(URLDecoder.decode("a","utf-8"));
	}
}
