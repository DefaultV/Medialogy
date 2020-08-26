using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PeriodicTable : MonoBehaviour {
	public GameObject tablet;
    public GameObject Hologram;
    public Transform SpawnPoint;

	// Use this for initialization
	void Start () {
        //Hologram.SetActive(false);
	}
	
	// Update is called once per frame
	void Update () {
		if (Input.GetKeyDown(KeyCode.I))
            SetHologramState(true);
        if (Input.GetKeyDown(KeyCode.O))
            SetHologramState(false);
}
	void OnTriggerEnter(Collider other){
		if(other.tag == "KillPlane"){
			tablet.transform.position = SpawnPoint.transform.position;
		}
	}

    void SetHologramState(bool state)
    {
        Hologram.SetActive(state);
    }
}