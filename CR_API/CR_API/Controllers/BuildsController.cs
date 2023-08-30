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
        public IEnumerable<Builds> Get()
        {
            using(QAOrgDBContext dBContext=new QAOrgDBContext())
            {
                return dBContext.Builds.ToList();
            }    
        }


        [Route("api/builds/getbuildtoday")]
        [HttpGet]
        public IEnumerable<Builds> GetBuildToday()
        {
            using (QAOrgDBContext dBContext = new QAOrgDBContext())
            {
                return dBContext.Builds.Where(x=>x.CreatedOn==DateTime.Today).ToList();
            }
        }
    }
}
