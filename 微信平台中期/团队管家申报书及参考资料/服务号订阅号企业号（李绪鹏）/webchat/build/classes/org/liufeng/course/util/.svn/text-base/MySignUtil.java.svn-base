package org.liufeng.course.util;

import java.io.IOException;
import java.util.Arrays;

import javassist.expr.NewArray;

import org.apache.commons.codec.binary.Base64;

import org.apache.commons.codec.digest.DigestUtils;
import org.junit.Test;

import com.qq.weixin.mp.aes.AesException;
import com.qq.weixin.mp.aes.WXBizMsgCrypt;
/**
 * 请求校验工具类
 * 
 * @author liufeng
 * @date 2013-05-18
 */
/*@Deprecated*/
public class MySignUtil{
	/*private MySignUtil(){}*/
	// 与接口配置信息中的Token要一致
	static String sToken = "QDG6eK";
	static String sCorpID = "wx5823bf96d3bd56c7";
	static String sEncodingAESKey = "jWmYm7qr5nMoAUwZRjGtBxmz3KA1tkAj3ykkR6q2B2C";
	public String a=new String("");
	public static WXBizMsgCrypt wxcpt=null;
	 static{
		 
			try {
				wxcpt = new WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID);
			} catch (AesException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
	 }
	 /*public static MySignUtil getInstance(){
		 if(instance==null){
			 instance=new MySignUtil();
		 }
		return instance;};
	 public static MySignUtil instance=new MySignUtil();
*/
	}