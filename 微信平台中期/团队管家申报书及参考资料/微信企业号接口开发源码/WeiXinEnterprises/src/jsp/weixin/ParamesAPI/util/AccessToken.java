package jsp.weixin.ParamesAPI.util;

/** 
 * ΢��ͨ�ýӿ�ƾ֤ 
 *  
 * @author Engineer-Jsp 
 * @date 2014.06.23 
 */  
public class AccessToken {  
    // ��ȡ����ƾ֤  
    private String token;  
    // ƾ֤��Чʱ�䣬��λ����  
    private int expiresIn;  
  
    public String getToken() {  
        return token;  
    }  
  
    public void setToken(String token) {  
        this.token = token;  
    }  
  
    public int getExpiresIn() {  
        return expiresIn;  
    }  
  
    public void setExpiresIn(int expiresIn) {  
        this.expiresIn = expiresIn;  
    }  
}  