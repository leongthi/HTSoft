using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using CR_API.Models;

namespace CR_API.Controllers
{
    public class BuildsController : ApiController
    {
        public IEnumerable<ws_Builds_List_Result> Get()
        {
            using(QAOrgEntities dBContext=new QAOrgEntities())
            {
                string Sess = "16FC6B61-3D5D-4DC5-8FBD-013FC42802C9";
                List<ws_Builds_List_Result> buildList = new List<ws_Builds_List_Result> ();

                buildList = dBContext.ws_Builds_List(Sess, 0).ToList();

                return buildList;
            }    
        }

    }
}
