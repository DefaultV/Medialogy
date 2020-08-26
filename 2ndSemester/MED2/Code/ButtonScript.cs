using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ButtonScript : MonoBehaviour {

	public AudioClip soundClip; 
	public GameObject left_controller;
	public GameObject right_controller;
	public AudioSource soundSource;

	// Use this for initialization
	void Start () {
		soundSource.clip = soundClip;

        atomStructure = GameObject.Find("InteractiveAtom").GetComponent<AtomScript>();
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKey(KeyCode.B) || getDistanceToControllers())
        {
            Button_Animate();
			GameObject.Find("Jukebox").GetComponent<AudioSource>().PlayOneShot (soundClip);
        }
        else
        {
            Deanim();
        }
	}
    public AtomScript atomStructure;
    float cd = 1f;
    public void Button_Animate()
    {
        transform.Find("button").GetComponent<Animator>().SetBool("ButtonPressAnim", true);
        //Debug.Log(transform.Find("button").GetComponent<Animator>().GetBool("ButtonPressAnim"));
        atomStructure.Purge();
    }
    void Deanim()
    {
        transform.Find("button").GetComponent<Animator>().SetBool("ButtonPressAnim", false);
    }

	bool getDistanceToControllers(){
		if (Vector3.Distance (transform.position, left_controller.transform.position) <= 1f) {
			return true;
		}
		if (Vector3.Distance (transform.position, right_controller.transform.position) <= 1f) {
			return true;
		}
		return false;
	}
}
