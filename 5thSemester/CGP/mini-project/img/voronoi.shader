Shader "watershader" {
    Properties{
        _MaxHeight("MaxHeight",float) = 1.0
            _WaterColor("Water Color", color) = (1.0,1.0,1.0,1.0)
            _Fresnel("Fresnel Power", float) = 0.2
            _FresnelContrast("Fresnel Contrast", float) = 1.0
            _Cube("Reflection Map", Cube) = "" {}
    }
    SubShader{
        Tags{ "Queue" = "Transparent"
        }
        GrabPass{ "_GrabTexture" }
        Pass{
            ZWrite Off
                Cull back
                //Blend SrcAlpha OneMinusSrcAlpha

                CGPROGRAM

#pragma vertex vert
#pragma fragment frag

#include "UnityCG.cginc"

                sampler2D _SurfTex;
            float4 _WaterColor;
            uniform float _MaxHeight;
            float _Fresnel;
            float _FresnelContrast;
            uniform samplerCUBE _Cube;
            sampler2D _GrabTexture;

            float3 random2( float3 p ) {
                return frac(sin(float3(dot(p,float3(127.1,311.7,58.01)),dot(p,float3(269.5,183.3,123.113)), dot(p, float3(127.1, 311.7, 58.01))))*43758.5453);
            }

            struct appdata{
                float4 vertex : POSITION;
                float4 texcoords : TEXCOORD0;
                float3 normals : NORMAL;
            };

            struct v2f{
                float4 vertex : SV_POSITION;
                float4 texcoords: TEXCOORD0;
                float4 colors : COLOR;
                float3 normals : NORMAL;
                float3 camDir : TEXCOORD1;
                float3 normalDir : TEXCOORD2;
                float3 viewDir : TEXCOORD3;
                float4 screenPos : TEXCOORD4;
            };



            // vertex shader
            v2f vert(appdata v){
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.texcoords = v.texcoords;
                o.normals = v.normals;

                float4x4 modelMatrix = unity_ObjectToWorld;
                float4x4 modelMatrixInv = unity_WorldToObject;
                float4 worldpos = normalize(mul(modelMatrix, v.vertex));
                float3 cam = normalize(_WorldSpaceCameraPos);
                //float3 viewDir = normalize(cam - worldpos);
                //o.normalDir = v.normals;//normalize(mul(float4(v.normals, 0.0), modelMatrixInv).xyz);
                o.viewDir = mul(modelMatrix, v.vertex).xyz
                    - _WorldSpaceCameraPos;
                o.normalDir = normalize(
                        mul(float4(v.normals, 0.0), modelMatrixInv).xyz);


                //o.camDir = cam;
                //o.viewDir = viewDir;

                float3 st = v.normals * 5.0;
                st.x = st.x;
                st.y = st.y;
                st.z = st.z;

                // tile the space
                float3 i_st = floor(st);
                float3 f_st = frac(st);

                float m_dist = 1.;
                float3 pointt = float3(0.0, 0.0, 0.0);

for (int y = -1; y <= 1; y++) {
    for (int x = -1; x <= 1; x++) {
        for (int z = -1; z <= 1; z++) {
            float3 neighbor = float3(float(x), float(y), float(z));
            pointt = random2(i_st + neighbor);
            pointt = 0.42 + 0.42*sin(_Time.y + 6.2831*pointt);
            float3 diff = float3(neighbor + pointt - f_st);
            float dist = length(diff);
            m_dist = min(m_dist, dist);
        }
    }
}

                float4 bump = float4(0.0, 0.0, 0.0, 1.0);
                bump = bump + m_dist;
                bump = float4(pow(bump.xyz, 3.0), 1.0);
                o.colors = bump;

float4 displacement = float4(v.normals * bump * _MaxHeight, 0.0) + v.vertex;
o.vertex = UnityObjectToClipPos(v.vertex + displacement*0.01);
o.screenPos = ComputeGrabScreenPos(o.vertex);
return o;
            }


            // fragment shader
            float4 frag(v2f i):COLOR{

                half fresnel = _Fresnel * pow(1.0 - dot(normalize(i.normalDir), normalize(i.viewDir)), _FresnelContrast);
                //half fresnel_2 = 1.25 * pow(1.0 + dot(normalize(i.normalDir), normalize(i.viewDir)), 2.0);

                i.screenPos += 0.3;
                float3 distortColor = tex2Dproj(_GrabTexture, i.screenPos);
                //distortColor *= _WaterColor;
                //fixed3 distortColor = tex2Dproj(_GrabTexture, i.screenPos);

                //return float4(distortColor, 1.0);
                float3 refractedDir = refract(i.viewDir, i.normals, 1.0/1.330);
                float3 reflectedDir = reflect(i.viewDir, i.normals);
                float d = 3.0;
                //return texCUBE(_Cube, reflectedDir);
                //return i.colors;
                //return texCUBE(_Cube, i.normals*1.5f);
                //float4 fresnel_2 = min(2.0, _WaterColor.a / abs(dot(i.viewDir, i.normals))*0.75);
                float trans = min(1.0 - pow(fresnel, 3.0), 1.0);
                float trans_refl = min(1.0 - pow(fresnel, 3.0), 1.0);
                float trans_refl2 = min(1.0 - pow(fresnel, 3.5), 1.0);
                trans_refl2 = (1 - trans_refl2);
                //_WaterColor.a = trans;
                _WaterColor.a = 1.0;
                //return _WaterColor;
                //return fresnel;
                //return (texCUBE(_Cube, refractedDir)*min((pow(fresnel, 6.0)), 1.0) + _WaterColor / d + i.colors / d);


return (float4(distortColor, 1.0)*(1 - trans)*.5) + (_WaterColor * trans)
	+ (min(i.colors, 1.0) / d) * trans_refl2*2.0 + i.colors/d
	+ (texCUBE(_Cube, reflectedDir) * trans_refl / d) * trans_refl2*2.0;// + (fresnel/2.0);

            }
            ENDCG
        }
    }
}
